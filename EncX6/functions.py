import time


def keeplog(content: str, log: bool = True) -> None:
    if log:
        date = time.strftime("%Y%m%d")
        with open("usedlog\\" + date + ".log", "a", encoding="utf-8") as f:
            f.write(content + "\n")
    else:
        pass


def cut(obj: str | list, sec: int) -> list:
    """实现字符串/列表按步平均切割。"""
    return [obj[i:i+sec] for i in range(0, len(obj), sec)]


def debug_print(content: str, debug: bool = False, log: bool = True) -> None:
    if debug:
        print("=================================\n"+content)
    else:
        pass
    keeplog(content, log)
