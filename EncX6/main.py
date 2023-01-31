"""
Author:       灰尘疾客
Date:         2023/01/16
OS Url:       https://github.com/gkcoll/EncX6
CN Meaning:   六重保镖
Introduction: 由一编码（Base 64）、五加密（凯撒 + 摩斯电码 + 范围表 + MD5 校验 + 栅栏），生成不是给人看的东西，理论上只要不要透露此程序，将没人能够知道你在发什么，尽管用上机器也不一定能得出加密原理。
Thanks:       Tester: Lanyu
Suggestion:   TThe developer advised you to import this module use simple code syntax like `import EncX6 as e6`.
"""
import EncX6.Caesar as Caesar
import EncX6.MorseCode as MorseCode
import EncX6.Base64_DIY as Base64
import EncX6.MD5 as MD5
import EncX6.Fence as Fence
from EncX6.functions import *
import EncX6.RangeTable as RangeTable
from time import strftime as s


def total_encrypt(content: str, caesar_key: int = 3, fence_key: int = 2) -> str:
    """总加密函数"""
    keeplog(s("%Y-%m-%d %H:%M:%S"))
    keeplog("加密内容:" + content)
    b64 = Base64.encode(content)
    caesar = Caesar.encrypt(b64, caesar_key)
    morse = MorseCode.encrypt(caesar)
    rand_enc = RangeTable.encrypt(morse_code=morse)
    added_md5 = MD5.add_md5(rand_enc)
    fence = Fence.encrypt(added_md5, fence_key)
    ciphertext = fence
    keeplog('********************')
    return ciphertext


def total_decrypt(ciphertext: str, caesar_key: int = 3, fence_key: int = 2) -> str:
    """总解密函数"""
    try:
        keeplog(s("%Y-%m-%d %H:%M:%S"))
        keeplog("解密内容:" + ciphertext)
        added_md5 = Fence.decrypt(ciphertext, fence_key)
        rand_dec = MD5.md5_verify(added_md5)
        if rand_dec == "Verifying ERROR":
            # MD5 验证不一致触发事件
            debug_print("MD5 校验错误，请检查密文是否完整")
            return "<!!!--Decrypted Error--!!!>"
        else:
            morse = RangeTable.decrypt(rand_dec)
            caesar = MorseCode.decrypt(morse)
            b64 = Caesar.decrypt(caesar, caesar_key)
            cleartext = Base64.decode(b64)
        keeplog('********************')
    except:
        return "<!!!--Decrypted Error--!!!>"
    else:
        return cleartext

def main():
    # You can add something for testing here.
    pass

if __name__ == "__main__":
    main()
