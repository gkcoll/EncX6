from EncX6.functions import debug_print as dbp


class morse():
    """一个简单的关于摩斯电码的类，支持手动/自动获取加密/解密结果。\n
    A simple class about MorseCode, it supported manual / auto get encrypted / decrypted result.\n
    2023/01/24"""

    def __init__(self, obj: str = "."):
        self.content = obj
        # 2023年1月24日，对字典进行补充完善，添加了几乎所有的标点符号的支持。
        # 注意：& 符的摩斯电码被修改过，原因：和字母 h 的相同。
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
        # 浅浅偷个懒，直接反转键-值的位置
        self._cleartext_dict = {v: k for k,v in self._ciphertext_dict.items()}
        # 这里设置两个属性方便直接调用（而不是直接调用下面的方法）
        self.ciphertext = self.get_ciphertext()
        self.cleartext = self.get_cleartext()
        self.auto = self.auto_get()

    def get_ciphertext(self) -> str:
        """用以返回传入参数的密文。"""
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
        """用以解密摩斯电码密文并返回明文。"""
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
        """根据传入数据自动判断返回密文或明文。注意：返回的是字典"""
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
                # 最后没有办法的办法
                return {"success": False,
                        "input": "Unknown",
                        "return": "message",
                        "result": "无法识别传入参数！",
                        "more_info": "暂时无法识别您传入的参数，请核对！如果传入明文请务必确保每个元素都在加密字典的键内！传入密文则需保证传入的为指定符号组成的密文！"}


def encrypt(obj: str) -> str:
    ciphertext = morse(obj).ciphertext
    if ciphertext:
        dbp("摩斯电码加密结果:" + ciphertext)
        return ciphertext
    else:
        dbp("摩斯电码加密错误！")


def decrypt(obj: str) -> str:
    cleartext = morse(obj).cleartext
    if cleartext:
        dbp("摩斯电码加密结果:" + cleartext)
        return cleartext
    else:
        dbp("摩斯电码加密错误！")


def auto(obj: str = "gkcoll") -> str:
    got = morse(obj).auto
    if got['success']:
        dbp("检测到输入类型为 " + got['input'] + ", 程序自动返回 " +
            got['return'] + "。结果: " + got['result'])
        return got['result']
    else:
        dbp("输入类型为 " + got['input'] + " , 返回类型为 " + got['return'] +
            " , 结果为: " + got['result'] + ' , 更多信息:\n  ' + got['more_info'])
        return None


if __name__ == "__main__":
    c = "oK!"
    e = "---/~*~/-.-.--"

    print(encrypt(c))
    print(decrypt(e))
    print(auto(c))
    print(auto(e))
    print(auto("."))
    print(bool(auto("你好")))  # 一个错误示例
