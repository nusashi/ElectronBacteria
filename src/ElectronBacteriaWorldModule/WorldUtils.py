# -*- coding: utf-8 -*-
# インポート

# pythonでバイナリを扱う際には文字列で表記される。その際に接頭辞として"0b"を追加しなければならない。

def testFunc(testParam):
    # 関数でのdocstringのサンプル
    """
    関数の説明を記述

    Parameters
    ----------
    testParam : string
        引数の説明を記述

    Returns
    -------
    returnParam : string
        返り値の説明を記述
    """
    returnParam = testParam
    print("parameter : " + testParam)
    print("return : " + testParam)
    return testParam

class testClass():
    # クラスでのdocstringのサンプル
    """
    クラス内の属性を記述

    Attributes
    ----------
    test_id : int
        属性の説明を記述
    test_name : string
        属性の説明を記述

    """
    def __init__(self, test_id):
        """
        コンストラクタの説明を記述

        Parameters
        ----------
        test_id : int
            引数の説明を記述

        Raises
        ------
        ValueError
            引数などが間違っていた場合
        
        See Also
        --------
        get_test_name : 最低限必要だと思われる関数や変数の説明を記述
        """
        self.test_id = test_id
        self.test_name = self.get_test_name(test_id = test_id)
    
    def get_test_name(self, test_id):
        """
        関数の説明を記述

        Parameters
        ----------
        test_id : int
            引数の説明を記述
        Returns
        -------
        test_name : string
            返り値の説明を記述
        """
        pass

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

# 2進数論理積関数 戻り値は整数
def binaryAndBinary(binary1,binary2):
    return int(bin(binary1 & binary2),0)

# 2進数論理和関数 戻り値は整数
def binaryOrBinary(binary1,binary2):
    return int(bin(binary1 | binary2),0)