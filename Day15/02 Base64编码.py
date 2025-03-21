# Base64的编码主要由64个符号组成：A-Z, a-z, 0-9, + /

import base64

s = 'you'

'''
逻辑：首先，base64是对于字节进行的编码
字符串 => 单个字符的 ASCII 码 => 找到这个字符在 ASCII 码里面的索引 => 
把这个索引数字用一个字符，也就是8个字节表示出来 =>
每 6 位一截断，得到的是 6 位的二进制数字 =>
2^6 = 64，利用这个数字，找到对应的 base64 编码

如果说我们的字符不能被6整除，自己补充一个空出来，然后切割，就ok，剩余的000用=补全
'''

s_encoded = s.encode()  # 处理成字节
s_base64_encoded = base64.b64encode(s_encoded)  # base64编码，得到字节
print(s_base64_encoded.decode())  # 解码成字符串

print(base64.b64encode('yo'.encode()).decode())     # eW8=
