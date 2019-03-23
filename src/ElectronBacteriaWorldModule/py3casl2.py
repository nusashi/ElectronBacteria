# -*- coding: utf-8 -*-

"""
PyCASL2, CASL II assembler implemented in Python.
Copyright (c) 2009, Masahiko Nakamoto.
All rights reserved.

Based on a simple implementation of CASL II assembler.
Copyright (c) 2001-2008, Osamu Mizuno.
"""
# インポート
import warnings
warnings.simplefilter('ignore',DeprecationWarning)

import sys, os, string, array, re
from optparse import OptionParser, OptionValueError
from sets import Set

op_tokens = Set(['NOP', 'LD', 'ST', 'LAD', 'ADDA', 'SUBA', 'ADDL', 'SUBL',
              'AND', 'OR','XOR', 'CPA', 'CPL', 'SLA', 'SRA', 'SLL', 'SRL',
              'JMI', 'JNZ', 'JZE', 'JUMP', 'JPL', 'JOV', 'PUSH', 'POP',
              'CALL', 'RET', 'SVC', 'START', 'END', 'DC', 'DS',
              'IN', 'OUT', 'RPUSH', 'RPOP'])

noarg, r, r1r2, adrx, radrx, ds, dc, strlen, start = [0, 1, 2, 3, 4, 5, 6, 7, 8]

reg_str = {}
for i in range(0,9):
    reg_str['GR%1d' % i] = i

# ニーモニックテーブル
op_table = {'NOP':[0x00, noarg],
            'LD2':[0x10, radrx],
            'ST':[0x11, radrx],
            'LAD':[0x12, radrx],
            'LD1':[0x14, r1r2],
            'ADDA2':[0x20, radrx],
            'SUBA2':[0x21, radrx],
            'ADDL2':[0x22, radrx],
            'SUBL2':[0x23, radrx],
            'ADDA1':[0x24, r1r2],
            'SUBA1':[0x25, r1r2],
            'ADDL1':[0x26, r1r2],
            'SUBL1':[0x27, r1r2],
            'AND2':[0x30, radrx],
            'OR2':[0x31, radrx],
            'XOR2':[0x32, radrx],
            'AND1':[0x34, r1r2],
            'OR1':[0x35, r1r2],
            'XOR1':[0x36, r1r2],
            'CPA2':[0x40, radrx],
            'CPL2':[0x41, radrx],
            'CPA1':[0x44, r1r2],
            'CPL1':[0x45, r1r2],
            'SLA':[0x50, radrx],
            'SRA':[0x51, radrx],
            'SLL':[0x52, radrx],
            'SRL':[0x53, radrx],
            'JMI':[0x61, adrx],
            'JNZ':[0x62, adrx],
            'JZE':[0x63, adrx],
            'JUMP':[0x64, adrx],
            'JPL':[0x65, adrx],
            'JOV':[0x66, adrx],
            'PUSH':[0x70, adrx],
            'POP':[0x71, r],
            'CALL':[0x80, adrx],
            'RET':[0x81, noarg],
            'SVC':[0xf0, adrx],
            'IN':[0x90, strlen],
            'OUT':[0x91, strlen],
            'RPUSH':[0xa0, noarg],
            'RPOP':[0xa1, noarg],
            'LD': [-1, 0],
            'ADDA':[-2, 0],
            'SUBA':[-3, 0],
            'ADDL':[-4, 0],
            'SUBL':[-5, 0],
            'AND':[-6, 0],
            'OR':[-7, 0],
            'XOR':[-8, 0],
            'CPA':[-9, 0],
            'CPL':[-10, 0],
            'START':[-100, start],
            'END':[-101, 0],
            'DS':[0, ds],
            'DC':[0, dc]}

''' unsigned -> signed '''
def l2a(x):
    x &= 0xffff
    if 0x0000 <= x <= 0x7fff:
        a = x
    elif 0x8000 <= x <= 0xffff:
        a = x - 2**16
    else:
        raise TypeError
    return a

''' signed -> unsigned '''
def a2l(x):
    x &= 0xffff
    if 0 <= x:
        return x
    return x + 2**16

class CASL2:

    class Label:
        def __init__(self, label, lines=0, filename='', addr=0, goto=''):
            self.label = label
            self.lines = lines
            self.filename = filename
            self.addr = addr
            self.goto = goto

        def __str__(self):
            scope, label = self.label.split('.')
            if len(scope) == 0:
                s = '{filename}:{lines}\t{addr:04x}\t{label}'.format(filename = self.filename, lines = self.lines, addr = self.addr, label = label)
            else:
                s = '{filename}:{lines}\t{addr:04x}\t{label} ({scope})'.format(filename = self.filename, lines = self.lines, addr = self.addr,  label = label, scope = scope)

            return s

    class Instruction:
        def __init__(self, label, op, args, line_number, src):
            self.label = label
            self.op = op
            self.args = args
            self.line_number = line_number
            self.src = src

        def __str__(self):
            return '{line_number}: {label}, {op}, {args}'.format(line_number = self.line_number, label = self.label, op = self.op, args = self.args)

    class ByteCode:
        def __init__(self, code, addr, line_number, src):
            self.code = code
            self.addr = addr
            self.line_number = line_number
            self.src = src

        def __str__(self):
            try:
                s = '{addr:04x}\t{code:04x}\t\t{line_number}\t{src}'.format(addr = self.addr, code = self.code[0], line_number = self.line_number, src = self.src)
            except IndexError:
                s = '%04x\t    \t\t%d\t%s'.format
                    (self.addr, self.line_number, self.src)
            if 1 < len(self.code):
                s += '\n'
                try:
                    s += '%04x\t%04x'.format
                        (self.addr+1, self.code[1])
                except TypeError:
                    s += '%04x\t%s'.format
                        (self.addr+1, self.code[1])
            if 2 < len(self.code):
                s += '\n'
                try:
                    s += '%04x\t%04x'.format
                        (self.addr+2, self.code[2])
                except TypeError:
                    s += '%04x\t%s'.format
                        (self.addr+2, self.code[2])
            return s

    class Error(Exception):
        def __init__(self, line_num, src, message):
            self.line_num = line_num
            self.src = src
            self.message = message

        def report(self):
            print("Error: %s\nLine %d: %s" % (self.message, self.line_num, self.src), file=sys.stderr)


