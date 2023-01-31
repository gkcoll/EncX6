from base64 import b64encode, b64decode
from EncX6.functions import debug_print as dbp
anti_counterfeit = ['gk', 'coll']


def encode(content: str = "Test") -> str:
    """实现 Base64 编码"""
    content_x = content.join(anti_counterfeit)  # 加防伪
    # 编码
    try:
        encoded = str(b64encode(content_x.encode('utf-8'))).strip("b'")
    except:
        dbp("Base64 编码错误")
    else:
        dbp("Base64加密结果:" + encoded)
        return encoded


def decode(encoded: str) -> str:
    """用以解码Base64编码内容。"""
    try:
        decoded = b64decode(encoded).decode("utf-8")
    except:
        dbp("Base64 解码错误")
    else:
        result = decoded.lstrip(
            anti_counterfeit[0]).rstrip(anti_counterfeit[1])
        dbp("Base64解密结果:" + result)
        return result
