'''
@File    :   functions.py
@Time    :   2023/02/12 20:00:54
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   Some common functions.
'''


import time


def keeplog(content: str) -> None:
    date = time.strftime("%Y%m%d")
    try:
        with open("usedlog\\" + date + ".log", "a", encoding="utf-8") as f:
            f.write(content + "\n")
    except FileNotFoundError:
        pass


def cut(obj: str | list, sec: int) -> list:
    """Cut str or list by step."""
    return [obj[i:i+sec] for i in range(0, len(obj), sec)]


def debug_print(content: str, debug: bool = False, log: bool = True) -> None:
    if debug:
        print("=================================\n"+content)
    else:pass
    keeplog(content)
