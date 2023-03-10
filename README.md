# [EncX6](https://github.com/gkcoll/EncX6)

[简体中文版](https://github.com/gkcoll/EncX6/blob/main/README_zh-CN.md) | [繁體中文版](https://github.com/gkcoll/EncX6/blob/main/README_zh-TW.md)

> ## Attention
> 
> If you find any conflict or ambiguity with this document in the readme file in other languages, [Simplified Chinese Version](https://github.com/gkcoll/EncX6/blob/README_zh-CN.md) shall prevail.

A simple text six-fold encryption algorithm that supports GUI.

<img src="https://hcjk.oss-cn-shenzhen.aliyuncs.com/img/encx6_RemovedBackground.png" title="" alt="程序图标" data-align="center">

## Introduction

Thanks for use this program. This program is wrote by Python. It supports GUI, small storage, one file, completely portable, **FREE TO USE**.

### About Naming

**This the story of the CN name**:

To be honest, the name of this project refers to the opinion of ChatGPT, the most popular AI recently. After all, I can't think of any meaningful name. In its results, the word "bodyguard" points out the confidentiality of the text, which is comparable to a safe. As long as the "bodyguard", also the key of the safe, is not disclosed/bought, the ciphertext will not be cracked.

<img src="https://hcjk.oss-cn-shenzhen.aliyuncs.com/img/%E7%96%BE%E5%AE%A2%E5%85%AD%E9%87%8D%E4%BF%9D%E9%95%96.png" title="" alt="Logo" data-align="center">

**About EN name**:

I summarized the common points of the two words:encoding and encryption - they have the  same letters group of "**enc**" in front of them. The short and exquisite "EncX6" is formed by capitalize them and adding an version code which means six-times - "**X6**".

### Project background

First of all, let's talk about an encrypted chat software project that was abandoned by me. It originally used RSA encryption, but found that it is not only difficult for users to configure, but also easy to stun users, so we should consider other methods.

Later, I came up with all kinds of ghost ideas, and also referred to the Morse code and Caesar code projects I had written. So I had a preliminary idea about this algorithm.

### Frame/library used

- [tkinter](https://github.com/python/cpython/tree/main/Lib/tkinter)
- [pyperclip](https://github.com/asweigart/pyperclip)
- [base64](https://github.com/python/cpython/blob/3.11/Lib/base64.py)

In addition, the executable program(only supports run on Windows, file type is `.exe`) was packed by [pyinstaller](https://github.com/pyinstaller/pyinstaller).

### Encryption Method

In fact, the project uses a total of one encoding method and five encryption methods, many of which were invented several centuries ago. Although there is a original encryption method (self think that) . But I can only hold the attitude of There is Always Someone Who is Better Than Us, And save the idea of may not find the founder.

The encoding method is Base64, and the others are listed in the following order of encryption:

- Caesar Cipher
- Morse Code
- Range Table Random Encryption
- MD5 Verify
- Fence Encryption

Many of these encryption methods are highly customized, which will be explained in detail later.

## Instructions

1. The ciphertext generated by this encryption algorithm can only (the developer really can't found dependent crack tools, so said that.) decrypt by the corresponding decryption algorithm(was provided). So please check that both you and the reciever(s) are have the tool before sending message at first.

2. After complying with the open source lisence, you can modify this program and repack, even republish it. The permissions include but are not limited to:
- Modify interface style
- Modify Caesar Cipher dictionary
- Modify Range Table
- Add more content(For example, you can increase the number of encryption layers)
- ...

The most important thing is that you should clone the warehouse by forking the project. Finally, you have to show the source and original developer (me) information in the finished program and readme file of your project:

| Parameter   | Value                                                                               |
| ----------- | ----------------------------------------------------------------------------------- |
| Developer   | [Albert Lin](https://github.com/gkcoll)                                             |
| Blog        | [Geek Collection](https://www.gkcoll.xyz)                                           |
| Project Url | [Github](https://github.com/gkcoll/EncX6) / [Gitee](https://gitee.com/gkcoll/EncX6) |

3. After downloading the contents of the  repositories, run the `main.py` directly. Please refer to the following table for other files and descriptions (in alphabetical order): 

| File          | Decription                                                               |
| ------------- | ------------------------------------------------------------------------ |
| Base64_DIY.py | Self-encapsulated Base64 encoding & decoding module                      |
| Caesar.py     | Caesar Cipher encrypt & decrypt module                                   |
| EncX6.py      | The main module of the program, incuded total encrypt & decrypt function |
| EncX6_GUI.py  | project's GUI program                                                    |
| fav.ico       | Icon                                                                     |
| Fence.py      | Fence encrypt & decrypt module                                           |
| functions.py  | functions module                                                         |
| ico.py        | Store the Base64 encoding of the icon file for loading after decryption  |
| MD5.py        | MD5 encrypt/decrypt & verify module                                      |
| MorseCode     | Morse Code encrypt & decrypt module                                      |
| RangeTable.py | Range Table Random encrypt & decrypt module                              |

Non-technical personnel can directly download the packaged distribution for use.

The distribution tutorial has been published in [My Blog](https://www.gkcoll.xyz), so there is no more verbose here.(that article have English version)

4. Repack: You can refer to the following code to call  `pyinstaller` for packaging (Please use the command  `pip install pyinstaller` to install `pyinstaller`):

```shell
pyinstaller -F main.py -i fav.ico -w --uac-admin
```

> Among them, `--uac-admin` is the command to obtain administrator privileges, because the program needs to call the system (use the os module) to delete files.

### About Terminal Mode

> Developers strongly recommend only using the terminal mode program as a module. The method of encryption and decryption only at the terminal provided in it is only used for debugging at the beginning, and then decided to use the GUI and gave up maintenance. Therefore, it is normal to encounter a bug during the use process, because there are many changes to the acceptance parameters of the total encryption/decryption function and other contents. If you need to use it, please modify the code yourself, and developers will not maintain it for the time being, Please regard the GUI program as standard.

Run `EncX6.py` as a program is well...

## Detailed Explanation of Encryption Method

1. Base64 encoding/decoding:

Call `b64encode` & `b64decode` in `base64` lib, add anti-counterfeiting verification for inputed content then encode it into utf-8 then for base64 encoding; decode process is decode it into utf-8 code then use base64 decode the result.

2. Caesar Cipher:

Move all the contents encrypted with Base64 according to the position of the key in the specified dictionary (which is actually a Python list), get the results in turn and then splice them back, and decrypt them in reverse (the key needs to be consistent).

3. Morse Code encryption:

In order to express full of the content, I was not satisfied with the dictionary of lowercase letters and numbers provided on web. I improved uppercase letters and add some punctuations(`+=/` , the three punctuation marks that may appear in Base64 encoding) by replacing characters.When encrypting, add the corresponding values in the dictionary in turn and add slashes(/), delete trailing slash after completion; When decrypting, divided content by slashes. Use `.split("/")` to split the content into a list, and then use the generator to generate a reverse dictionary (key: value ->value: key) about Morse Code encryption dictionary for query, and then return the substring of the values found in the reverse dictionary.

4. Range Table Random encryption

The ciphertext generated by the Morse Code above will be composed of the following symbols at most: `._/*~`, So I collected all the keys that can be found on the keyboard (excluding the ones with escape meaning), and finally cut these things (scrambled) into a list of elements of equal length with the encapsulated `cut` function as the range table, and then replace the above symbols with any one of the corresponding elements in the range table in turn; Decryption is also very simple. It only needs to parse the original symbols according to their positions and return them to Morse Code for further decryption.

5. MD5 Verify:

This step is **very important**. It directly makes the ciphertext content that can be infinitely random generated from the previous step unique - further calculate the MD5 value of the ciphertext obtained from the previous step, and set the threshold for the decryption process before and after splitting the 32-bit content into half ciphertext: after the MD5 is spliced back, calculate whether the MD5 of the middle ciphertext is the same as the previous MD5. If it is different, it will return an error, and if it is the same, it will continue. Of course, this step is also very simple and can only increase the complexity of the text. As long as you can decompile, you can directly delete the relevant code and skip it.

6. Fence encryption

This is the last trump card of this algorithm. When encrypting, it arranges the ciphertext wrapped by MD5 shifts in two columns (according to the key, you can choose more or less, and fill in the position if the get modular has a value), and finally vertically splices them in order to return the fenced content. Decryption is a reverse operation. There is nothing to say. It disrupts the arrangement of MD5 and range table encrypted ciphertext, ~~confuses the vision~~ and increases the difficulty of machine crack - let alone makes it difficult for the machine to find the ciphertext rule.

## API Index

> Sort by execution order or importance.
> 
> As an open source project, all functions here can be rewritten or inherited.
> 
> When used as a module, directly use the `import` keyword to import methods/functions/variables into the project.

### EncX6

**Introduction**: Main module.

#### total_encrypt & total_decrypt

**Introduction**: Total encryption & total decryption functions

**Required parameter(s)**:

- content: What to encrypt, string(for total_encrypt)

- ciphertext: What to decrypt, string(for total_decrypt)

**Optional parameters**

- caesar_key: Caesar Cipher key, incoming 3 if nothing incomed, integer

- fence_key: Fence Encryption, Incoming 2 if nothing incomed, integer

**Return**: string

#### Base64_DIY

**Introduction**: DIY Base64 encode & decode module.

##### encode & decode

**Introduction**: encode & decode function.

**Required parameter(s)**:

- content: What to encode, string(for encode)

- encoded: What to decode, string or bytes(for decode)

**Return**: string

#### Caesar

**Introduction**: Caesar Cipher encrypt & decrypt module 

##### encrypt & decrypt

**Introduction**: encryption & decryption funtion

**Required parameter(s)**:

- content: What to encrypt, string(for encrypt)

- ciphertext: What to decrypt, string(for decrypt)

**Optional parameters**:

- key: Caesar Cipher key(the displacement), incoming 3 if not incomed, integer

**Return**: string

#### MorseCode

**Introduction**: Morse Code encrypt & decrypt module.

##### encrypt & decrypt

**Introduction**: The encryption & decryption function.

**Required parameter(s)**：

- obj: Content that need to process, string(for both encrypt & decrypt)

**Return**: string

##### morse

**Introduction**: A simple class made with reference to the basic data types, used for Morse Code processing.

**Required parameter(s)**: obj: Content what need to process.

**Callable properties**：

- ciphertext: The ciphertext of content, string

- cleartext: Decryption result for the ciphertext, string

- content: Original text(return the incoming things), string

- auto: Auto, dict

**Callable methods**:

- get_ciphertext: get the ciphertext of the content, string

- get_cleartext: get the cleartext of the ciphertext, string

- auto_get: Auto get content of target type, dict

#### RangeTable

**Introduction**: Range Table Random encryption's encrypt & decrypt module.

##### encrypt & decrypt

**Introduction**: The encryption & decryption function.

**Required parameter(s)**:

- content: What to encrypt, string(for encrypt)

- ciphertext: What to decrypt, string(for decrypt)

**Return**: string

#### MD5

**Introduction**: Functions required by the program about MD5.

##### md5

**Introduction**: Encapsulated md5 value calculation function.

**Required parameter(s)**: content: What to calculate.

**Return**: MD5 value, string

##### add_md5

**Introduction**: A function used for add half the md5 value before and after the content.

**Required parameter(s)**: content: What to add.

**Return**: Processed results, string

##### md5_verify

**Introduction**: md5 verifying function.

**Required parameter(s)**: content: Content generated by `add_md5` functions.

**Return**: Success: What been encrypted; Fail: Error message

#### Fence

**Introduction**: Fence encryption's encrypt & decrypt module.

##### encrypt & decrypt

**Introduction**: encryption & decryption functions

**Required parameter(s)**: 

- content: What to encrypt, string(for encrypt)

- encryption: What to decrypt, string(for decrypt)

**Optional parameters**: key: Fence encryption key, incoming default 2 if nothing incomed, integer

#### functions

**Introduction**: Common functions module

##### cut

**Introduction**: Function to cut string / list evenly by step.

**Required parameter(s)**：

- obj: Object to process, string or list

- sec: step, The length of each element after cutting, integer

**Return**: list

##### debug_print

**Introduction**: A special print function for debuging, encapsulated `print` and add a switch for controlling, make it **controllable**.

**Required parameter(s)**: 

- content: What to output, string

**Optional parameters**：

- debug: The switch for debuging print, related to output or not. default `False` , bool

- log: The switch of recording log, related to record or not, default `True` , bool

**Return**: 

```python
None
```

##### keeplog

**Introduction**: Log recording function

**Required parameter(s)**: content: The content to output to the log file.

**Optional parameters**: log: The switch of recording log, related to record or not, default `True` , bool

**Return**: 

```python
None
```

## Lisence

This project follows the xx open source license.Users must follow this License.

## Thanks to

At the end of the document, I have to point out and thanks to these contributers whom gave many helps to the developer with this project. THANKS SO MUCH! :)

1. @Lanyu(Tester, Adviser, ~~Developer~~)
