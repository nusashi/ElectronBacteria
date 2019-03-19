# -*- coding: utf-8 -*-
# インポート
import os
from src.ElectronBacteriaWorldModule import SampleCode as sc
from src.ElectronBacteriaWorldModule import WorldUtils as wu


def main():
    print(wu.binaryStringToInt("1001"))
    print(wu.binaryStringToInt("1011"))
    print(wu.binaryAndBinary(9,11))
    test()

# 関数宣言
def test():
    sc.testFunc("1029")
    sc.whileLoopTest()




# メイン関数
if __name__ == '__main__':
    main()
