'''
@File    :   MorseCode.py
@Time    :   2023/02/12 20:02:28
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   An advanced Morse Code module.
'''


from EncX6.functions import debug_print as dbp


class morse():
    """A simple class about MorseCode, it supported manual / auto get encrypted / decrypted result.
    2023/01/24"""

    def __init__(self, obj: str = "."):
        self.content = obj
        # 2023年1月24日，对字典进行补充完善，添加了几乎所有的标点符号的支持。
        # 注意：& 符的MorseCode被修改过，原因：和字母 h 的相同。
        self._ciphertext_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
                                 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                                 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
                                 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                                 'y': '-.--', 'z': '--..',
                                 'A': '*~', 'B': '~***', 'C': '~*~*', 'D': '~**', 'E': '*', 'F': '**~*',
                                 'G': '~~*', 'H': '****', 'I': '**', 'J': '*~~~', 'K': '~*~', 'L': '*~**',
                                 'M': '~~', 'N': '~*', 'O': '~~~', 'P': '*~~*', 'Q': '~~*~', 'R': '*~*',
                                 'S': '***', 'T': '~', 'U': '**~', 'V': '***~', 'W': '*~~', 'X': '~**~',
                                 'Y': '~*~~', 'Z': '~~**',
                                 '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                                 '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                                 '/': '-..-.', '+': '.-.-.', '=': '-...-', '.': '.-.-.-', ':': '---...',
                                 ',': '--..--', ';': '-.-.-.', '?': '..--..', '\'': '.----.', '!': '-.-.--',
                                 '-': '-....-', '_': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-',
                                 '$': '...-..-', '&': '......', '@': '.--.-.'}
        self._cleartext_dict = {v: k for k,v in self._ciphertext_dict.items()}
        # Three attributes for could calling directly..
        self.ciphertext = self.get_ciphertext()
        self.cleartext = self.get_cleartext()
        self.auto = self.auto_get()

    def get_ciphertext(self) -> str:
        """Return Ciphertext of incoming parameter."""
        try:
            ciphertext = str()
            for letter in self.content:
                ciphertext += self._ciphertext_dict[letter] + "/"
            ciphertext = ciphertext.rstrip("/")
        except KeyError:
            return None
        else:
            return ciphertext

    def get_cleartext(self) -> str:
        """For decrypt ciphertext and return cleartext."""
        try:
            cleartext = str()
            ciphertext_of_letters = self.content.split("/")
            for code in ciphertext_of_letters:
                cleartext += self._cleartext_dict[code]
        except KeyError:
            return None
        else:
            return cleartext

    def auto_get(self) -> dict:
        """Automatically determine whether to return ciphertext or plaintext based on the incoming data. Attention: Returned is a dict"""
        if self.cleartext:
            return {"success": True,
                    "input": "ciphertext",
                    "return": "cleartext",
                    "result": self.cleartext}
        else:
            if self.ciphertext:
                return {"success": True,
                        "input": "content",
                        "return": "ciphertext",
                        "result": self.ciphertext}
            else:
                return {"success": False,
                        "input": "Unknown",
                        "return": "message",
                        "result": "The incoming parameter is not recognized!",
                        "more_info": "The parameter you incomed in cannot be recognized temporarily, please check! If you pass in clear text, make sure that every element is in the key of the encryption dictionary! When passing in ciphertext, you need to ensure that the incoming ciphertext is composed of the specified symbols!"}


def encrypt(obj: str) -> str:
    ciphertext = morse(obj).ciphertext
    if ciphertext:
        dbp("MorseCode encryption result: " + ciphertext)
        return ciphertext
    else:
        dbp("MorseCode encrypting error! ")


def decrypt(obj: str) -> str:
    cleartext = morse(obj).cleartext
    if cleartext:
        dbp("MorseCode decryption result: " + cleartext)
        return cleartext
    else:
        dbp("MorseCode decrypting error!")


def auto(obj: str = "gkcoll") -> str:
    got = morse(obj).auto
    if got['success']:
        dbp("Input type detected is " + got['input'] + ", Auto return " +
            got['return'] + ". Result: " + got['result'])
        return got['result']
    else:
        dbp("Input a " + got['input'] + " , Return " + got['return'] +
            " , Result: " + got['result'] + ' , More:\n  ' + got['more_info'])
        return None


if __name__ == "__main__":
    c = "oK!"
    e = "---/~*~/-.-.--"

    print(encrypt(c))
    print(decrypt(e))
    print(auto(c))
    print(auto(e))
    print(auto("."))
    print(bool(auto("你好")))  # A mistake example.
