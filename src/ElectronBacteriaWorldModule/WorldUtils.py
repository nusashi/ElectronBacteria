# -*- coding: utf-8 -*-
# インポート

# pythonでバイナリを扱う際には文字列で表記される。その際に接頭辞として"0b"を追加しなければならない。

def binaryStringToInt(binaryString):
    """
    文字列の"101"などの2進数を整数型の10進数に変換する。

    Parameters
    ----------
    binaryString : string
        2進数で表現された数値文字列

    Returns
    -------
    int("0b" + binaryString,0) : int
        引数のバイナリ文字列をint型の整数として返す。
    """
    return int("0b" + binaryString,0)

def binaryAndBinary(binary1,binary2):
    """
    2進数論理積関数

    Parameters
    ----------
    binary1 : int
        2進数表記の整数型
    binary2 : int
        2進数表記の整数型
    Returns
    -------
    int(bin(binary1 & binary2),0) : int
        引数のbinary1とbinary2の論理積をint型の整数として返す。
    """
    return int(bin(binary1 & binary2),0)

def binaryOrBinary(binary1,binary2):
    """
    2進数論理和関数

    Parameters
    ----------
    binary1 : int
        2進数表記の整数型
    binary2 : int
        2進数表記の整数型

    Returns
    -------
    int(bin(binary1 | binary2),0) : int
        引数のbinary1とbinary2の論理和をint型の整数として返す。
    """

    return int(bin(binary1 | binary2),0)