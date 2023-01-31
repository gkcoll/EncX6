"""不管网上是否有相关加解密方式，反正这套加解密方式是没有参考任何内容，暂且认它个原创吧！"""

from EncX6.functions import debug_print as dbp
from EncX6.functions import cut
from random import randint
letters = cut(
    "l#AjU,6)tQ;*c0n`|of_P>JG!ux.W?'b8%KX~IZgzhi4/3$BrS-]:@s7T[9&dH<(aCeMqvRpVFENy2w^O+5=mYD1Lk", 15)



def encrypt(morse_code: str) -> str:
    """实现自定义的范围表随机加密 | 由 ChatGPT 重构"""
    try:
        replace_map = {'.': "1", '-': "2", '*': "3", '~': "4", '/': "5"}
        replaced_morse = "".join(replace_map.get(c, c)
                                 for c in morse_code[::-1])
        # 补齐 4 的倍数个字符以便后续操作
        replaced_morse += "6" * (4 - len(replaced_morse) % 4)
        # 使用随机数在范围内随机抽取元素添加
        ciphertext = "".join(letters[int(
            c) - 1][randint(0, 14)] for c in replaced_morse)
    except:
        dbp("加密失败，可能用了非法字符！")
    else:
        dbp("疾客范围表随机加密结果:" + ciphertext)
        return ciphertext


def decrypt(ciphertext: str) -> str:
    """实现自定义的范围表随机加密的解密 | 由 ChatGPT 重构"""
    try:
        letter_map = {letter: str(index + 1) for index, letter_group in enumerate(
            letters) for letter in letter_group}
        replaced_morse = "".join(letter_map.get(c, c) for c in ciphertext)
        # 删除末尾的补位符6并翻转列表，最后替换回摩斯电码后拼接成明文
        cleartext = "".join("." if c == "1" else "-" if c == "2" else "*" if c == "3" else "~" if c ==
                             "4" else "/" if c == "5" else c for c in replaced_morse.rstrip("6")[::-1])
    except:
        dbp("解密失败，可能用了非法字符！")
    else:
        dbp("疾客范围表解密结果:" + cleartext.rstrip("/"))
        return cleartext.rstrip("/")
