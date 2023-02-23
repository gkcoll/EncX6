'''
@File        :   main.py
@Time        :   2023/02/18 16:28:18
@Author      :   @灰尘疾客
@Version     :   1.0
@Site        :   https://www.gkcoll.xyz
@Desc        :   One encoding method (Base 64) and five encryption methods (Caesar + MorseCode + RangeTable + MD5Verify + Fence) generate a non-visible thing. 
                 In theory, if you only want to disclose this program, no one will know what you are sending, although the encryption principle may not be obtained by using the machine.
@Thanks      :   Tester: Lanyu
@Suggestion  :   The developer advised you to import this module use simple code syntax like `import EncX6 as e6`.

'''



import EncX6.Caesar as Caesar
import EncX6.MorseCode as MorseCode
import EncX6.Base64_DIY as Base64
import EncX6.MD5 as MD5
import EncX6.Fence as Fence
from EncX6.functions import *
import EncX6.RangeTable as RangeTable
import time


def total_encrypt(content: str, caesar_key: int = 3, fence_key: int = 2) -> str:
    """Total encryption function."""
    keeplog(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    keeplog("Ciphertext:" + content)
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
    """Total decryption function."""
    try:
        keeplog(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        keeplog("Cleartext:" + ciphertext)
        added_md5 = Fence.decrypt(ciphertext, fence_key)
        rand_dec = MD5.md5_verify(added_md5)
        if rand_dec == "Verifying ERROR":
            # MD5 verification inconsistency trigger event
            debug_print("MD5 Varifying Error! Please check the integrity of ciphertext..")
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
