# -*- coding: utf-8 -*-
# インポート
from pynput.keyboard import Key, Controller
from pynput import keyboard

# pythonでバイナリを扱う際には文字列で表記される。その際に接頭辞として"0b"を追加しなければならない。
# pythonでは定数構文が無い為、大文字+スネーク記法で記述して習慣とする。

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
    print("return : " + returnParam)
    return returnParam

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
        # 処理
        return test_id

def whileLoopTest():
    while True:
        pass
        
    pass

    
def keyboardControllTest():

    cKeyboard = Controller()

    # Press and release space
    cKeyboard.press(Key.space)
    cKeyboard.release(Key.space)

    # Type a lower case A; this will work even if no key on the
    # physical keyboard is labelled 'A'
    cKeyboard.press('a')
    cKeyboard.release('a')

    # Type two upper case As
    cKeyboard.press('A')
    cKeyboard.release('A')
    with cKeyboard.pressed(Key.shift):
        cKeyboard.press('a')
        cKeyboard.release('a')

    # Type 'Hello World' using the shortcut type method
    cKeyboard.type('Hello World')

def MonitoringKeyboardTest():
    pass

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# # リスナーを立ち上げてイベントを見張る為、最後に実行するタイプの記述
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
