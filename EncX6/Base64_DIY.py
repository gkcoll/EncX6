'''
@File    :   Base64_DIY.py
@Time    :   2023/02/12 18:39:02
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   A customized base64 module.
'''


from base64 import b64encode, b64decode
from EncX6.functions import debug_print as dbp
anti_counterfeit = ['gk', 'coll']


def encode(content: str = "Test") -> str:
    """Base64 encode function."""
    content_x = content.join(anti_counterfeit)  # Add anti-counterfeit identification
    # Encoding
    try:
        encoded = str(b64encode(content_x.encode('utf-8'))).strip("b'")
    except:
        dbp("Base64 encoding error!")
    else:
        dbp("Base64 encoding error!: " + encoded)
        return encoded


def decode(encoded: str) -> str:
    """Base64 decode function."""
    try:
        decoded = b64decode(encoded).decode("utf-8")
    except:
        dbp("Base64 decoding error!")
    else:
        result = decoded.lstrip(
            anti_counterfeit[0]).rstrip(anti_counterfeit[1])
        dbp("Base64 decoding error: " + result)
        return result
