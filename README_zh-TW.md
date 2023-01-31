# [EncX6](https://github.com/gkcoll/EncX6)

[English Version](https://github.com/gkcoll/EncX6) | [简体版](https://github.com/gkcoll/EncX6/README_zh-CN.md)

> ## Attention/注意
> 
> If you find any conflict or ambiguity with this document in the readme file in other languages, [Simplified Chinese Version](https://github.com/gkcoll/EncX6/blob/README_zh-CN.md) shall prevail.
> 
> 若您在其他語言版本的自述檔案裏發現與本檔案有衝突或不明確，一律以[簡體中文版](https://github.com/gkcoll/EncX6/blob/README_zh-CN.md)為准。

一個簡單的文字六重加密演算法，支持含圖形使用者介面（GUI）。

<img src="https://hcjk.oss-cn-shenzhen.aliyuncs.com/img/encx6_RemovedBackground.png" title="" alt="程序图标" data-align="center">

## 介紹

首先感謝使用本程式，本程式由Python編寫，帶圖形使用者介面，體積較小，單檔案，完全可以便攜使用。

### 命名原則

實不相瞞，本項目的名字參攷了最近火爆的人工半智障——ChatGPT的意見，畢竟自己實在想不到有什麼有意義的名字。 在其給的結果中，“保鏢”一詞點出對文字的保密力度，堪比保險箱。 只需不洩露/收買這個“保鏢”，亦是保險箱的鑰匙，密文（ciphertext）就不會被破解。

<img src="https://hcjk.oss-cn-shenzhen.aliyuncs.com/img/%E7%96%BE%E5%AE%A2%E5%85%AD%E9%87%8D%E4%BF%9D%E9%95%96.png" title="" alt="Logo" data-align="center">

### 項目背景

首先是某被我弃坑的加密聊天軟體項目，原本用的是 RSA 加密，但是發現對於用戶不僅配寘麻煩，更易繞暈用戶，所以弃用，另考慮他法。
後來想到了各種鬼點子，還去參攷曾經寫過的摩斯電碼和凱撒密碼的項目，於是我對本算灋有了初步的想法。

### 所用框架/庫

- [tkinter](https://github.com/python/cpython/tree/main/Lib/tkinter)
- [pyperclip](https://github.com/asweigart/pyperclip)
- [base64](https://github.com/python/cpython/blob/3.11/Lib/base64.py)

另外，可執行程式（僅支持Windows系統，檔案類型為 `.exe`）使用 [pyinstaller](https://github.com/pyinstaller/pyinstaller) 進行打包。

### 加密方式

其實按理說，本項目共用的是一種編碼方式和五種加密方式，其中的很多加密方式都是幾世紀前就為人所發明，儘管有一個自稱原創的加密方式，但是也只能持天外有天的態度，保留可能是找不到創始人的想法。

編碼方式就是Base64，其它的按加密順序排列如下：

- 凱撒加密

- 摩斯電碼加密

- 範圍錶隨機加密

- MD5加密驗證

- 柵欄加密

其中很多加密管道做了高度的自定義化，後面會詳細說明。

## 使用說明

1. 由本加密算法加密的內容基本只能（開發者實在找不到相關的破解工具，只能這麼說了）用本算灋對應的解密算灋解開，所以如需用到資訊傳遞，請提前將工具（編譯好）發送給接收消息的對方。

2. 你可以在遵守開源協定的情况下，對本程式進行修改後重新發佈，許可權包括但不僅限於：
- 修改介面樣式
- 修改凱撒密碼字典
- 修改範圍錶字典
- 新增更多內容（如新增加密層數）
- ……

而最關鍵的是，你應該通過fork本項目的管道尅隆本倉庫，最後你得在你的項目的成品程式和自述檔案裏出現出處和原創開發者（我）的資訊：

| 參數   | 值                                                                                   |
| ---- | ----------------------------------------------------------------------------------- |
| 開發者  | [灰尘疾客](https://github.com/gkcoll)                                                   |
| Blog | [极客藏源](https://www.gkcoll.xyz)                                                      |
| 項目地址 | [Github](https://github.com/gkcoll/EncX6) / [Gitee](https://gitee.com/gkcoll/EncX6) |

3. 下载仓庫內容后直接运行 `main.py` 即可，其它文件和描述请参照下表（排序按首字母顺序）：

| 文件            | 描述                       |
| ------------- | ------------------------ |
| Base64_DIY.py | 自行封裝的 Base64 編解碼模塊       |
| Caesar.py     | 凱撒密碼加解密模塊                |
| EncX6.py      | 程式主模塊，內有總加/解密函數          |
| EncX6_GUI.py  | 程式圖形使用者介面程式              |
| fav.ico       | 圖標                       |
| Fence.py      | 柵欄加解密模塊                  |
| functions.py  | 函數檔案                     |
| ico.py        | 存放圖標檔案的 Base64 編碼以便解密後加載 |
| MD5.py        | MD5 加解密&驗證模塊             |
| MorseCode     | 摩斯電碼加解密模塊                |
| RangeTable.py | 範圍錶隨機加密/解密模塊             |

非科技人員可直接下載打包好的發行版本使用。
發行版本使用教程在我的 [Blog](https://www.gkcoll.xyz) 已有發佈，此處不多囉嗦——

```shell
pyinstaller -F main.py -i fav.ico -w --uac-admin
```

> 其中 `--uac-admin` 為獲取管理員許可權命令，因為程式需要調用系統（使用 os 模塊）刪除檔。

### 關於終端模式

> 開發者強烈推薦僅將終端模式程式作為模塊使用，裡面所提供的僅在終端進行加解密的管道僅為當初調試使用，後來决定使用圖形使用者介面後便放弃維護了，所以在使用過程中遇到 BUG 很正常，因為總加密/解密函數的接受參數等其它內容改了很多，如需使用，請自行修改程式碼，開發者就暫時懶得維護了， 請各位以 GUI 介面程式為標準。

直接將 `EncX6.py` 作為程式運行即可……

## 加密方式詳解

1. Base64 編解碼：

調用 Base64 庫的`b64encode` & `b64decode`，將輸入的內容加上防偽驗證後轉化為 utf-8 編碼後傳入進行編碼，解碼則先解碼成 utf-8 編碼再解碼。

2. 凱撒加密：

將用 Base64 加密的內容全部按 key 在指定字典（實為 Python list）中的位置進行位移，依次得出結果後拼接返回，解密則反向操作（key 需一致）。

3. 摩斯電碼加密：

為了能够完整地表示內容，我不滿於網上提供的小寫字母字典和數位字典，我通過替換字元的管道完善了大寫字母的表示並補充了一些標點符號（+=/，即 Base64 編碼的三個標點符號）。加密時依次添加字典中對應的值並添加斜杠（/），完畢後删除末尾的斜杠；解密時按照斜杠為劃分，使用 `.split("/")` 將內容折開為清單，再通過生成器（generator）生成關於摩斯電碼字典的反向字典（key:value -> value:key）用於査詢，再返回從反向字典中依次查找出的值拼接的子字串。

4. 範圍錶隨機加密：

上面的摩斯電碼加密出來的結果最多會由以下幾種符號組成：`._/*~`，故我凑齊了鍵盤上能找到的所有按鍵（排除有轉義意義的），最後用封裝的 `cut` 函數將這些東西（打亂過）平均切成元素等長度的清單作為範圍錶，再依次將上面的符號替換為範圍錶中對應元素中的任意一個字元； 解密也很簡單，僅需按位置分別解析出原本的符號，交回摩斯電碼進一步解密即可。

5. MD5 加密驗證：

這一步很關鍵，直接讓原本由上一步生成的可以無限隨機的密文內容變得唯一——將上一步得出的密文進一步算出 MD5 值，將這 32 位的內容分半各加密文前後，解密過程再設定門檻：MD5 拼接回來後計算中間密文的 MD5 是否與前面的 MD5 一樣，不一樣則返回錯誤，一樣則繼續。 當然這一步也很簡陋，只能讓新增文字複雜度，只要會反編譯則可直接删除相關程式碼跳過。

6. 柵欄加密：

這是本算灋的最後一張王牌——它加密時將被MD5分班包裹的密文進行雙欄（根據 key ，可多可少，取模有值則補位）排列，最後依次垂直拼接，返回被柵欄化處理的內容。解密則是反向操作，沒啥好說。 打亂了MD5與範圍錶加密密文的排列，~~混淆視覺~~，增加機器破解難度——少說讓機器不好找出密文規律。

## API 索引

> 排序按執行先後或重要性排序。
> 作為開源項目，這裡所有的函數都可重寫或繼承。
> 在作為模塊使用的時候，直接使用 `import` 關鍵字將方法/函數/變數導入工程使用即可。

### EncX6

**介紹**：主模塊。

#### total_encrypt & total_decrypt

**介紹**：總加密函數和總解密函數

**必須參數**：

- content：要加密之內容，string（for total_encrypt）

- ciphertext：要解密之內容，string（for total_decrypt）

**可選參數**

- caesar_key：凱撒加密 key ，不傳入則默認傳入3，integer

- fence_key：柵欄加密 key ，不傳入則默認傳入 2，integer

**返回**：string

#### Base64_DIY

**介紹**：自定義的 Base64 編解碼模塊。

##### encode & decode

**介紹**：編碼和解碼函數

**必須參數**：

- content：要編碼的內容，string（for encode）

- encoded：要解碼的內容，string/bytes（for decode）

**返回**：string

#### Caesar

**介紹**：凱撒加解密模塊。

##### encrypt & decrypt

**介紹**：加密和解密函數

**必須參數**：

- content：要加密的內容，string（for encrypt）

- ciphertext：要解密的內容，string（for decrypt）

**可選參數**：

- key：凱撒加密 key ，不傳入則默認傳入 3，integer

**返回**：string

#### MorseCode

**介紹**：摩斯电码加解密模塊

##### encrypt & decrypt

**介紹**：加密和解密函數

**必要參數**：

- obj：要處理的內容，string（for both encrypt & decrypt）

**返回**：string

##### morse

**介紹**：參攷基礎資料類型做出的簡單的類

**必須參數**：obj：要處理的內容

**可調用的属性**：

- ciphertext：密文，string

- cleartext：明文，string

- content：原文，string

- auto：自動，dict

**可調用的方法**：

- get_ciphertext：獲取密文，string

- get_cleartext：獲取明文，string

- auto_get：自動獲取目標類型內容，dict

#### RangeTable

**介紹**：範圍錶隨機加解密模塊。

##### encrypt & decrypt

**介紹**：加密和解密函數

**必須參數**：

- content：要加密的內容，string（for encrypt）

- ciphertext：要解密的內容，string（for decrypt）

**返回**：string

#### MD5

**介紹**：程式所需的關於 md5 操作的函數。

##### md5

**介紹**：封裝的 md5 計算函數

**必須參數**：content：要計算的內容

**返回**：md5 內容，string

##### add_md5

**介紹**：為內容左右添加 md5 各半的函數

**必須參數**：content：要添加的內容

**返回**：處理好的結果，string

##### md5_verify

**介紹**：md5 驗證函數

**必須參數**：content：由 `add_md5` 函數生成的內容

**返回**：成功：被加密的內容；失敗：錯誤消息

#### Fence

**介紹**：柵欄加解密模塊。

##### encrypt & decrypt

**介紹**：加密和解密函數

**必要參數**：

- content：要加密的內容，string（for encrypt）

- ciphertext：要解密的內容，string（for decrypt）

**可選參數**：key：柵欄加密 key ，不傳入則傳入預設值 2，integer

#### functions

**介紹**：常用函數模塊

##### cut

**介紹**：按步平均切割 string/list 的函數。

**必要參數**：

- obj：要處理的對象，string/list

- sec：步，切割後各元素的長度，integer

**返回**：list

##### debug_print

**介紹**：調試輸出，封裝了 `print` ，使之可控

**必須參數**：

- content：輸出內容，string

**可選參數**：

- debug：調試輸出的開關，關係到是否輸出，默認為 `False` ，bool

- log：日誌開關，關係到是否輸出，默認為 `True` ，bool

**返回**：

```python
None
```

##### keeplog

**介紹**：記錄日誌函數

**必須參數**：content：要輸出到日誌檔的內容。

**可選參數**：log：日誌開關，關係到是否輸出，默認為 `True` ，bool

**返回**：

```python
None
```

## 許可證

本項目遵循 xx 開源協定，請使用者務必遵循該協定。

## Thanks to

At the end of the document, I have to point out and thanks to these contributers whom gave many helps to the developer with this project. THANKS SO MUCH! :)

1. @Lanyu（Tester, Adviser, ~~Developer~~）
