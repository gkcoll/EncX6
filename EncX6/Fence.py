'''
@File    :   Fence.py
@Time    :   2023/02/12 20:00:14
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   Fence encryption module.
'''


from EncX6.functions import cut
from EncX6.functions import debug_print as dbp


def encrypt(content: str, key: int = 2) -> str:
    """Fence encryption function."""
    if len(content) % key:
        # Multiple characters of the number of completion lines.
        content += "@" * (key - (len(content) % key))
    strings = cut(content, key)

    # The logic of the following code is very complicated. If necessary, you can use pen and paper to calculate
    ciphertext = str()
    for index in range(key):
        for item in strings:
            ciphertext += item[index]
    dbp("Fence encrypt result:" + ciphertext)
    return ciphertext


def decrypt(encryption: str, key: int = 2) -> str:
    strings = cut(encryption, int(len(encryption)/key))

    # The logic of the following code is very complicated. If necessary, you can use pen and paper to calculate
    cleartext = str()
    for index in range(int(len(encryption)/key)):
        for item in range(key):
            cleartext += strings[item][index]

    cleartext = cleartext.rstrip("@")
    dbp("Fence decrypt result:" + cleartext)
    return cleartext
