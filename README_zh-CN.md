# [EncX6](https://github.com/gkcoll/EncX6)

[English Version](https://github.com/gkcoll/EncX6) | [繁體版](https://github.com/gkcoll/EncX6/blob/main/README_zh-TW.md)

> ## Attention/注意
> 
> If you find any conflict or ambiguity with this document in the readme file in other languages, this document (Simplified Chinese Version) shall prevail.
> 
> 若您在其他语言版本的自述文件里发现与本文档有冲突或不明确，一律以本文档（简体中文版）为准。 

一个简单的文本六重加密算法，支持含图形用户界面（GUI）。

<img src="https://hcjk.oss-cn-shenzhen.aliyuncs.com/img/encx6_RemovedBackground.png" title="" alt="程序图标" data-align="center">

## 介绍

首先感谢使用本程序，本程序由 Python 编写，带图形用户界面，体积较小，单文件，完全可以便携使用。

### 命名原则

实不相瞒，本项目的名字参考了最近火爆的人工半智障 —— ChatGPT 的意见，毕竟自己实在想不到有什么有意义的名字。在其给的结果中，“保镖”一词点出对文本的保密力度，堪比保险箱。只需不泄露/收买这个“保镖”，亦是保险箱的钥匙，密文（ciphertext）就不会被破解。

<img src="https://hcjk.oss-cn-shenzhen.aliyuncs.com/img/%E7%96%BE%E5%AE%A2%E5%85%AD%E9%87%8D%E4%BF%9D%E9%95%96.png" title="" alt="Logo" data-align="center">

### 项目背景

首先是某被我弃坑的加密聊天软件项目，原本用的是 RSA 加密，但是发现对于用户不仅配置麻烦，更易绕晕用户，所以弃用，另考虑他法。

后来想到了各种鬼点子，还去参考曾经写过的摩斯电码和凯撒密码的项目，于是我对本算法有了初步的想法。

### 所用框架/库

* [tkinter](https://github.com/python/cpython/tree/main/Lib/tkinter)
* [pyperclip](https://github.com/asweigart/pyperclip)
* [base64](https://github.com/python/cpython/blob/3.11/Lib/base64.py)

另外，可执行程序（仅支持 Windows 系统，文件类型为 `.exe`）使用 [pyinstaller](https://github.com/pyinstaller/pyinstaller) 进行打包。

### 加密方式

其实按理说，本项目共用的是一种编码方式和五种加密方式，其中的很多加密方式都是几世纪前就为人所发明，尽管有一个自称原创的加密方式，但是也只能持天外有天的态度，保留可能是找不到创始人的想法。

编码方式就是 Base64，其它的按加密顺序排列如下：

* 凯撒加密
* 摩斯电码加密
* 范围表随机加密
* MD5 加密验证
* 栅栏加密

其中很多加密方式做了高度的自定义化，后面会详细说明。

## 使用说明

1. 由本加密算法加密的内容基本只能（开发者实在找不到相关的破解工具，只能这么说了）用本算法对应的解密算法解开，所以如需用到信息传递，请提前将工具（编译好）发送给接收消息的对方。

2. 你可以在遵守开源协议的情况下，对本程序进行修改后重新发布，权限包括但不仅限于：
* 修改界面样式
* 修改凯撒密码字典
* 修改范围表字典
* 新增更多内容（如增加加密层数）
* ……

而最关键的是，你应该通过 fork 本项目的方式克隆本仓库，最后你得在你的项目的成品程序和自述文件里出现出处和原创开发者（我）的信息：

| 参数   | 值                                                                                   |
|:----:|:-----------------------------------------------------------------------------------:|
| 开发者  | [灰尘疾客](https://github.com/gkcoll)                                                   |
| 博客   | [极客藏源](https://www.gkcoll.xyz)                                                      |
| 项目地址 | [Github](https://github.com/gkcoll/EncX6) / [Gitee](https://gitee.com/gkcoll/EncX6) |

3. 下载仓库内容后直接运行 `main.py` 即可，其它文件和描述请参照下表（排序按首字母顺序）：

| 文件            | 描述                       |
|:-------------:|:------------------------:|
| Base64_DIY.py | 自行封装的 Base64 编解码模块       |
| Caesar.py     | 凯撒密码加解密模块                |
| EncX6.py      | 程序主模块，内有总加/解密函数          |
| EncX6_GUI.py  | 程序图形用户界面程序               |
| fav.ico       | 图标                       |
| Fence.py      | 栅栏加解密模块                  |
| functions.py  | 函数文件                     |
| ico.py        | 存放图标文件的 Base64 编码以便解密后加载 |
| MD5.py        | MD5 加解密 & 验证模块           |
| MorseCode     | 摩斯电码加解密模块                |
| RangeTable.py | 范围表随机加密/解密模块             |

非技术人员可直接下载打包好的发行版使用。

发行版使用教程在我的[博客](https://www.gkcoll.xyz)里已有发布，此处不多哔哔——

4. 重新打包：可以参考以下代码调用 `pyinstaller` 进行打包（若没有请先使用这条命令进行安装 `pip install pyinstaller`）：

```shell
pyinstaller -F main.py -i fav.ico -w --uac-admin
```

> 其中 `--uac-admin` 为获取管理员权限命令，因为程序需要调用系统（使用 os 模块）删除文件。

### 关于终端模式

> 开发者强烈推荐仅将终端模式程序作为模块使用，里面所提供的仅在终端进行加解密的方式仅为当初调试使用，后来决定使用图形用户界面后便放弃维护了，所以在使用过程中遇到 BUG 很正常，因为总加密/解密函数的接受参数等其它内容改了很多，如需使用，请自行修改代码，开发者就暂时懒得维护了，请各位以 GUI 界面程序为标准。

直接将 `EncX6.py` 作为程序运行即可……

## 加密方式详解

1. Base64 编解码：

调用 Base64 库的 `b64encode` & `b64decode`，将输入的内容加上防伪验证后转化为 utf-8 编码后传入进行编码，解码则先解码成 utf-8 编码再解码。

2. 凯撒加密：

将用 Base64 加密的内容全部按密钥在指定字典（实为 Python 列表）中的位置进行位移，依次得出结果后拼接返回，解密则反向操作（密钥需一致）。

3. 摩斯电码加密：

为了能够完整地表示内容，我不满于网上提供的小写字母字典和数字字典，我通过替换字符的方式完善了大写字母的表示并补充了一些标点符号（+=/，即 Base64 编码的三个标点符号）。加密时依次添加字典中对应的值并添加斜杠（/），完毕后删除末尾的斜杠；解密时按照斜杠为划分，使用 `.split("/")` 将内容拆分为列表，再通过生成器（generator）生成关于摩斯电码字典的反向字典（key:value -> value:key）用于查询，再返回从反向字典中依次查找出的值拼接的子字符串。

4. 范围表随机加密：

上面的摩斯电码加密出来的结果最多会由以下几种符号组成：._/*~，故我凑齐了键盘上能找到的所有按键（排除有转义意义的），最后用封装的 cut 函数将这些东西（打乱过）平均切成元素等长度的列表作为范围表，再依次将上面的符号替换为范围表中对应元素中的任意一个字符；解密也很简单，仅需按位置分别解析出原本的符号，交回摩斯电码进一步解密即可。

5. MD5 加密验证：

这一步很关键，直接让原本由上一步生成的可以无限随机的密文内容变得唯一——将上一步得出的密文进一步算出 MD5 值，将这 32 位的内容分半各加密文前后，解密过程再设置门槛：MD5 拼接回来后计算中间密文的 MD5 是否与前面的 MD5 一样，不一样则返回错误，一样则继续。当然这一步也很简陋，只能让增加文本复杂度，只要会反编译则可直接删除相关代码跳过。

6. 栅栏加密：

这是本算法的最后一张王牌——它加密时将被 MD5 分班包裹的密文进行双栏（根据密钥，可多可少，取模有值则补位）排列，最后依次垂直拼接，返回被栅栏化处理的内容。解密则是反向操作，没啥好说。打乱了 MD5 与范围表加密密文的排列，~~混淆视觉~~，增加机器破解难度——少说让机器不好找出密文规律。

## API 索引

> 排序按执行先后或重要性排序。
> 
> 作为开源项目，这里所有的函数都可重写或继承。
> 
> 在作为模块使用的时候，直接使用 `import` 关键字将方法/函数/变量导入工程使用即可。

### EncX6

**介绍**：主模块。

#### total_encrypt & total_decrypt

**介绍**：总加密函数和总解密函数

**必须参数**：

- content：要加密内容，字符串（for total_encrypt）

- ciphertext：要解密的内容，字符串（for total_decrypt）

**可选参数**

- caesar_key：凯撒加密密钥，不传入则默认传入 3，整数

- fence_key：栅栏加密密钥，不传入则默认传入 2，整数

**返回**：字符串

#### Base64_DIY

**介绍**：自定义的 Base64 编解码模块。

##### encode & decode

**介绍**：编码和解码函数

**必须参数**：

- content：要编码的内容，字符串（for encode）

- encoded：要解码的内容，字符串或字节（for decode）

**返回**：字符串

#### Caesar

**介绍**：凯撒加解密模块。

##### encrypt & decrypt

**介绍**：加密和解密函数

**必须参数**：

- content：要加密的内容，字符串（for encrypt）

- ciphertext：要解密的内容，字符串（for decrypt）

**可选参数**：

- key：凯撒加密密钥，不传入则默认传入 3，整数

**返回**：字符串

#### MorseCode

**介绍**：摩斯电码加解密模块

##### encrypt & decrypt

**介绍**：加密和解密函数

**必要参数**：

- obj：要处理的内容，字符串（for both encrypt & decrypt）

**返回**：字符串

##### morse

**介绍**：参考基础数据类型做出的简单的类

**必须参数**：obj：要处理的内容

**可调用的属性**：

- ciphertext：密文，字符串

- cleartext：明文，字符串

- content：原文，字符串

- auto：自动，字典

**可调用的方法**：

- get_ciphertext：获取密文，字符串

- get_cleartext：获取明文，字符串

- auto_get：自动获取目标类型内容，字典

#### RangeTable

**介绍**：范围表随机加解密模块。

##### encrypt & decrypt

**介绍**：加密和解密函数

**必须参数**：

- content：要加密的内容，字符串（for encrypt）

- ciphertext：要解密的内容，字符串（for decrypt）

**返回**：字符串

#### MD5

**介绍**：程序所需的关于 md5 操作的函数。

##### md5

**介绍**：封装的 md5 计算函数

**必须参数**：content：要计算的内容

**返回**：md5内容，字符串

##### add_md5

**介绍**：为内容左右添加 md5 各半的函数

**必须参数**：content：要添加的内容

**返回**：处理好的结果，字符串

##### md5_verify

**介绍**：md5 验证函数

**必须参数**：content：由 `add_md5` 函数生成的内容

**返回**：成功：被加密的内容；失败：错误消息

#### Fence

**介绍**：栅栏加解密模块。

##### encrypt & decrypt

**介绍**：加密和解密函数

**必要参数**：

- content：要加密的内容，字符串（for encrypt）

- ciphertext：要解密的内容，字符串（for decrypt）

**可选参数**：key：栅栏加密密钥，不传入则传入默认值 2，整数

#### functions

**介绍**：常用函数模块

##### cut

**介绍**：按步平均切割字符串/列表的函数。

**必要参数**：

- obj：要处理的对象，字符串或列表

- sec：步，切割后各元素的长度，整数

**返回**：列表

##### debug_print

**介绍**：调试输出，封装了 `print` ，使之可控

**必须参数**：

- content：输出内容，字符串

**可选参数**：

- debug：调试输出的开关，关系到是否输出，默认为 `False` ，布尔

- log：日志开关，关系到是否输出，默认为 `True` ，布尔

**返回**：

```python
None
```

##### keeplog

**介绍**：记录日志函数

**必须参数**：content：要输出到日志文件的内容。

**可选参数**：log：日志开关，关系到是否输出，默认为 `True` ，布尔

**返回**：

```python
None
```

## 许可证

本项目遵循 xx 开源协议，请使用者务必遵循该协议。

## Thanks to

At the end of the document, I have to point out and thanks to these contributers whom gave many helps to the developer with this project. THANKS SO MUCH! :)

1. @Lanyu（Tester, Adviser, ~~Developer~~）
