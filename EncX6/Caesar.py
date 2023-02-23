'''
@File    :   Caesar.py
@Time    :   2023/02/12 19:59:06
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   Caesar Cipher module(A displacement encryption method).
'''


from EncX6.functions import debug_print as dbp
caesar_list = "oMQUmaBrV0lIjg1dyu2ntZ3bNWS4XYpT5DkPRh6iLz7vKfJ8sqOH9EGFcACwex"


def encrypt(content: str, key: int = 3) -> str:
    """Caesar encryption function."""
    ciphertext = str()
    try:
        for i in content:
            if i in caesar_list:
                ciphertext += caesar_list[(
                    caesar_list.index(i) + key) % len(caesar_list)]
            else:
                ciphertext += i
    except:
        dbp("Caesar encrypting FAILD!")
    else:
        dbp("Caesar encrypt result:" + ciphertext)
        return ciphertext


def decrypt(ciphertext: str, key: int = 3) -> str:
    """Caesar decryption function."""
    cleartext = str()
    try:
        for i in ciphertext:
            if i in caesar_list:
                cleartext += caesar_list[(
                    caesar_list.index(i) - key) % len(caesar_list)]
            else:
                cleartext += i
    except:
        dbp("Caesar decrypt FAILD!")
    else:
        dbp("Caesar decrypting result:" + cleartext)
        return cleartext
