from EncX6.functions import debug_print as dbp
caesar_list = "oMQUmaBrV0lIjg1dyu2ntZ3bNWS4XYpT5DkPRh6iLz7vKfJ8sqOH9EGFcACwex"


def encrypt(content: str, key: int = 3) -> str:
    """用以对字符串进行移位加密，即凯撒密码"""
    ciphertext = str()
    try:
        for i in content:
            if i in caesar_list:
                ciphertext += caesar_list[(
                    caesar_list.index(i) + key) % len(caesar_list)]
            else:
                ciphertext += i
    except:
        dbp("凯撒密码加密出错！")
    else:
        dbp("凯撒加密结果:" + ciphertext)
        return ciphertext


def decrypt(ciphertext: str, key: int = 3) -> str:
    """用以解密凯撒密码加密的内容"""
    cleartext = str()
    try:
        for i in ciphertext:
            if i in caesar_list:
                cleartext += caesar_list[(
                    caesar_list.index(i) - key) % len(caesar_list)]
            else:
                cleartext += i
    except:
        dbp("凯撒密码解密错误！")
    else:
        dbp("凯撒解密结果:" + cleartext)
        return cleartext
