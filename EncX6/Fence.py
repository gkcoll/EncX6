from EncX6.functions import cut
from EncX6.functions import debug_print as dbp


def encrypt(content: str, key: int = 2) -> str:
    if len(content) % key:
        # 补齐行数的倍数个字符
        content += "@" * (key - (len(content) % key))
    strings = cut(content, key)

    # 以下代码的逻辑很绕，必要时候可拿笔纸演算
    ciphertext = str()
    for index in range(key):
        for item in strings:
            ciphertext += item[index]
    dbp("栅栏加密结果:" + ciphertext)
    return ciphertext


def decrypt(encryption: str, key: int = 2) -> str:
    strings = cut(encryption, int(len(encryption)/key))

    # 以下代码的逻辑更绕，必要时候可拿笔纸演算
    cleartext = str()
    for index in range(int(len(encryption)/key)):
        for item in range(key):
            cleartext += strings[item][index]

    cleartext = cleartext.rstrip("@")
    dbp("栅栏解密结果:" + cleartext)
    return cleartext
