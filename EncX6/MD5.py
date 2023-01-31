import hashlib
from EncX6.functions import debug_print as dbp
from EncX6.functions import cut


def md5(content: str) -> str:
    """简单封装一下 MD5 计算的函数。"""
    obj = hashlib.md5()
    obj.update(content.encode(encoding='utf-8'))
    dbp("MD5计算结果:" + obj.hexdigest())
    return obj.hexdigest()


def add_md5(content: str) -> str:
    """为字符串加上 MD5 增一道防伪"""
    md5_splited = cut(md5(content), 16)
    result = md5_splited[0] + content + md5_splited[1]
    dbp("MD5分割拼接结果:" + result)
    return result


def md5_verify(content: str) -> str:
    """MD5 验证"""
    md5_splited = [content[0:16], content[-16:]]
    md5_encryption = "".join(md5_splited)
    # Fixed bug: 2023/01/19, change the way to remove string: *strip -> replace
    be_encrypted = content.replace(md5_splited[0], "").replace(md5_splited[1], "")
    if md5(be_encrypted) == md5_encryption:
        dbp("MD5 验证成功..")
        return be_encrypted
    else:
        return "Verifying ERROR"
