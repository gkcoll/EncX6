'''
@File    :   MD5.py
@Time    :   2023/02/12 20:01:58
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   Customized MD5 module.
'''


import hashlib
from EncX6.functions import debug_print as dbp
from EncX6.functions import cut


def md5(content: str) -> str:
    """MD5 calculation function."""
    obj = hashlib.md5()
    obj.update(content.encode(encoding='utf-8'))
    dbp("MD5 value:" + obj.hexdigest())
    return obj.hexdigest()


def add_md5(content: str) -> str:
    """Add MD5 value for str."""
    md5_splited = cut(md5(content), 16)
    result = md5_splited[0] + content + md5_splited[1]
    dbp("MD5 splicing result:" + result)
    return result


def md5_verify(content: str) -> str:
    """MD5 verification function."""
    md5_splited = [content[0:16], content[-16:]]
    md5_encryption = "".join(md5_splited)
    # Fixed bug: 2023/01/19, change the way to remove string: *strip -> replace
    be_encrypted = content.replace(md5_splited[0], "").replace(md5_splited[1], "")
    if md5(be_encrypted) == md5_encryption:
        dbp("MD5 verifying successfully..")
        return be_encrypted
    else:
        return "Verifying ERROR"
