'''
@File    :   EncX6_GUI.py
@Time    :   2023/02/12 20:04:50
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   GUI Core file of the project. 
'''


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
    t_out.delete("1.0", "end")  # Empty input box.
    if content.strip() != "":
        print("---\nEncrypting: " + content)
        encryption = total_encrypt(
            content, keys['caesar_key'], keys['fence_key'])
        if encryption_verify(encryption):
            t_out.insert("end", encryption)
            print("---\nCiphertext:" + encryption)
        else:
            print("Ciphertext verifying error! See more details in log, and contact the developer if you need.")
            keeplog("Error! If you need help, please send this file to the developer! Email: 2736550029@qq.com")
    else:
        print("---\nEncryption is performed but no content entered..")
        t_out.insert("end", "Not entered!!")
    t_out.config(state=DISABLED)


def decrypt():
    keys = read_keys()
    t_out.config(state=NORMAL)
    content = t_in.get("1.0", "end").strip()
    t_out.delete("1.0", "end")
    if content.strip() != "":
        print("---\nDecrypting: " + content)
        decryption = total_decrypt(
            content, keys['caesar_key'], keys['fence_key'])
        if decryption != "<!!!--Decrypted Error--!!!>":
            t_out.insert("end", decryption)
            print("---\nCleartext: " + decryption)
        else:
            print("---\nDecryption failed! Please check the possibility of errors, such as incorrect ciphertext, inconsistent key, incomplete ciphertext, etc.")
            keeplog("Decryption failed! Possible input is not due to ciphertext, inconsistent ciphertext, incomplete ciphertext, etc. Contact the developer is you need: 2736550029@qq.com.")
            t_out.insert("end", "Decryption failed!")
            showerror(title="Decryption failed!",message="It is possible that the input is not caused by the ciphertext or the key is inconsistent or the ciphertext is incomplete\nContact the developer if you need.")
        
    else:
        print("---\nDecryption is performed but no content is entered..")
        t_out.insert("end", "Not entered!!")
    t_out.config(state=DISABLED)


def encryption_verify(encryption):
    keys = read_keys()
    content = t_in.get('1.0', 'end').strip()
    # encryption = t_out.get('1.0', 'end').strip()
    try:
        decryption = total_decrypt(
            encryption, keys['caesar_key'], keys['fence_key'])
    except:
        showerror(title="Verifying Error", message="The ciphertext decryption verification failed (decryption failed). The message may have errors with the actual situation, for reference only.")
    else:
        if decryption == content:
            return True
        else:
            showerror(title="Verifying Error", message="The ciphertext decryption verification failed (the content is inconsistent). The message may have errors with the actual situation, for reference only.")


def copy():
    result = t_out.get('1.0', 'end').strip()
    pyperclip.copy(result)
    print("---\nA copy was performed..")


# intializing..
print("Opening, wait a moment...")
win = Tk()

# 设置窗口属性并居中
win.title("GK EncX6 | by @灰尘疾客 (www.gkcoll.xyz)")
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
ww = 500
wh = 500
x = (sw-ww) / 2
y = (sh-wh) / 2
win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
win.resizable(0, 0)

# Set icon.
with open("fav.ico", "wb+") as pic:
    pic.write(base64.b64decode(ico))
win.iconbitmap('fav.ico')
os.remove("fav.ico")

# Two neccessary keys getting boxes.
# Caesar Cipher.
# Set notice label.
l_cs_key = Label(win, width=10, height=2, fg="#001616",
                 font=('楷体', 13), text="Caesar Key")
l_cs_key.place(x=15, y=1)
# Set Caesar key input box.
cs_key = StringVar()
e_cs_key = Entry(win, show=None, font=('Arial', 14), textvariable=cs_key)
cs_key.set("3")  # Set default value as 3.
e_cs_key.place(x=115, y=7)

# Fence Encryption
# Set notice label.
l_fence_key = Label(win, width=10, height=2, fg="#001616",
                    font=('楷体', 13), text="Fence Key")
l_fence_key.place(x=15, y=40)
# Set Fence key input box.
fc_key = StringVar()
e_fence_key = Entry(win, show=None, font=('Arial', 14), textvariable=fc_key)
fc_key.set("2")  # Set default value as 2.
e_fence_key.place(x=115, y=47)

# Set content input box.
t_in = Text(win, height=7, font=('仿宋', 13))
t_in.pack(padx=25, pady=90)

# Set encryption button.
b_enc = Button(win, text='Encrypt', font=('华文行楷', 15),
               width=10, height=1, command=encrypt)
b_enc.place(x=150, y=265, anchor='s')

# Set decryption button.
b_dec = Button(win, text='Decrypt', font=('华文行楷', 15),
               width=10, height=1, command=decrypt)
b_dec.place(x=350, y=265, anchor='s')

# Set a result output box.
t_out = Text(win, height=12, width=64, font=('宋体', 10), bg="#d3f1ff")
t_out.config(state=DISABLED)
t_out.place(x=25, y=280)

# Set a button for copy result.
b_copy = Button(win, text='COPY', font=('黑体', 15,),
                fg="red", width=12, height=1, command=copy)
b_copy.place(x=398, y=490, anchor='s')

# Show window.
print("---\nEnjoy yourself！")
win.mainloop()
print("---\nExited..")
time.sleep(3)

