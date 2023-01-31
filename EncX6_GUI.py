import base64
from EncX6 import total_encrypt, total_decrypt, keeplog
from fav import ico
import os
import pyperclip
import time
from tkinter import *
from tkinter.messagebox import *


def read_keys():
    config = dict()
    caesar_key = e_cs_key.get()
    fence_key = e_fence_key.get()
    config['caesar_key'] = int(caesar_key)
    config['fence_key'] = int(fence_key)
    return config


def encrypt():
    keys = read_keys()
    t_out.config(state=NORMAL)
    content = t_in.get("1.0", "end").strip()
    t_out.delete("1.0", "end")  # 清空输出框
    if content.strip() != "":
        print("---\n执行加密，加密内容: " + content)
        encryption = total_encrypt(
            content, keys['caesar_key'], keys['fence_key'])
        if encryption_verify(encryption):
            t_out.insert("end", encryption)
            print("---\n加密结果: " + encryption)
        else:
            print("密文验证失败！详情请见日志，如需帮助请联系开发者！")
            keeplog("出现错误！如需帮助请将本文件发送给开发者！邮箱：2736550029@qq.com")
    else:
        print("---\n执行加密但并未输入内容..")
        t_out.insert("end", "未输入！！")
    t_out.config(state=DISABLED)


def decrypt():
    keys = read_keys()
    t_out.config(state=NORMAL)
    content = t_in.get("1.0", "end").strip()
    t_out.delete("1.0", "end")
    if content.strip() != "":
        print("---\n执行解密，解密内容: " + content)
        decryption = total_decrypt(
            content, keys['caesar_key'], keys['fence_key'])
        if decryption != "<!!!--Decrypted Error--!!!>":
            t_out.insert("end", decryption)
            print("---\n解密结果: " + decryption)
        else:
            print("---\n解密失败! 请排查一下出错的可能，如输入的不是密文、密钥不一致、密文不完整等……")
            keeplog("解密失败！可能输入的不是密文或密文不一致、密文不完整等原因所致，如需帮助请联系开发者邮箱：2736550029@qq.com")
            t_out.insert("end", "解密失败！")
            showerror(title="解密失败！",message="可能输入的不是密文或密钥不一致或密文不完整等原因所致，\n如需帮助请联系开发者！")
        
    else:
        print("---\n执行解密但并未输入内容..")
        t_out.insert("end", "未输入！！")
    t_out.config(state=DISABLED)


def encryption_verify(encryption):
    keys = read_keys()
    content = t_in.get('1.0', 'end').strip()
    # encryption = t_out.get('1.0', 'end').strip()
    try:
        decryption = total_decrypt(
            encryption, keys['caesar_key'], keys['fence_key'])
    except:
        showerror(title="验证失败", message="密文解密验证失败（解密失败），消息可能与实际情况有误差，仅供参考")
    else:
        if decryption == content:
            return True
        else:
            showerror(title="验证失败", message="密文解密验证失败（内容不一致），消息可能与实际情况有误差，仅供参考")


def copy():
    result = t_out.get('1.0', 'end').strip()
    pyperclip.copy(result)
    print("---\n执行了一次复制..")


# 初始化
print("正在打开，请稍后...")
win = Tk()

# 设置窗口属性并居中
win.title("疾客六重保镖 | by @灰尘疾客 (www.gkcoll.xyz)")
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
ww = 500
wh = 500
x = (sw-ww) / 2
y = (sh-wh) / 2
win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
win.resizable(0, 0)

# 设置图标
with open("fav.ico", "wb+") as pic:
    pic.write(base64.b64decode(ico))
win.iconbitmap('fav.ico')
os.remove("fav.ico")

# 两个必要的密钥获取框
# 凯撒密码
# 设置提示标签
l_cs_key = Label(win, width=8, height=2, fg="#001616",
                 font=('楷体', 13), text="凯撒密钥")
l_cs_key.place(x=22, y=1)
# 设置凯撒密码密钥输入框
cs_key = StringVar()
e_cs_key = Entry(win, show=None, font=('Arial', 14), textvariable=cs_key)
cs_key.set("3")  # 设置默认值为 3
e_cs_key.place(x=110, y=7)

# 栅栏加密
# 设置提示标签
l_fence_key = Label(win, width=8, height=2, fg="#001616",
                    font=('楷体', 13), text="栅栏密钥")
l_fence_key.place(x=22, y=40)
# 设置凯撒密码密钥输入框
fc_key = StringVar()
e_fence_key = Entry(win, show=None, font=('Arial', 14), textvariable=fc_key)
fc_key.set("2")  # 设置默认值为 2
e_fence_key.place(x=110, y=47)

# 设置内容文本输入框
t_in = Text(win, height=7, font=('仿宋', 13))
t_in.pack(padx=25, pady=90)

# 设置加密按钮
b_enc = Button(win, text='加密', font=('金山云技术体', 15),
               width=10, height=1, command=encrypt)
b_enc.place(x=150, y=265, anchor='s')

# 设置解压按钮
b_dec = Button(win, text='解密', font=('金山云技术体', 15),
               width=10, height=1, command=decrypt)
b_dec.place(x=350, y=265, anchor='s')

# 设置文本编辑框作结果输出框
t_out = Text(win, height=12, width=64, font=('宋体', 10), bg="#d3f1ff")
t_out.config(state=DISABLED)
t_out.place(x=25, y=280)

# 设置一个复制结果的按钮
b_copy = Button(win, text='复制结果', font=('钉钉进步体', 15,),
                fg="red", width=12, height=1, command=copy)
b_copy.place(x=398, y=490, anchor='s')

# 显示窗口
print("---\n打开完毕，Enjoy yourself！")
win.mainloop()
print("---\n已退出！")
time.sleep(3)
