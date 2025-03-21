from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

'''

首先，加密算法分为对称加密和非对称加密：是否使用同一套 key 来进行加密和解密

对称加密算法：AES, DES

在 AES 中，存在两种 加密模式：CBC 和 ECB

CBC：更加复杂，需要一个 key 和一个 iv
ECB：只需要一个 key

'''

'''

key的长度：
(最常用) 16：AES-128
(其次)  32：AES-192
(最次)  24：AES-256

后面的数字其实是字节数，一个字符8个比特位，所以后面跟的就是字节数量

iv的长度只能是 16 位

加密模式：
(1) ECB模式：比较简单，给定一个字符串，然后根据 key 的长度进行切割，然后分成一个个 block，单独加密再拼接
(2) CBC模式：也分成block，只不过这次，前一组的密文会和后面一组的明文做异或操作，然后再进行加密然后再拼接

不管是什么模式，他们都不会像 MD5 一样，改一点动全部

'''

# (1) 确定参数，构建对象

'''
参数：MODE，KEY，IV
'''

key = '1234567890123456'.encode()
iv = 'asdfghjklzxcvbnm'.encode()
# 当然，有些网站的这个key或者iv是直接写死的字节，不是通过encode转过去的，无所谓

aes_obj = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)

# (2) 加密
data = 'I am Kevin!'.encode()
# print(len(data))    # 11

# 由于我们设置了 key 是16位，所以必须要满足一个条件：data的字节数是16的整数倍，所以我们需要用到函数pad和unpad来解决
new_data = pad(data, 16)
# print(new_data)

# 加密
encrypt_data = aes_obj.encrypt(new_data)
print(encrypt_data)     # b'-:\xbb+\xbe=\x82\xe7\xfe\x80l\xcb&EP\xde'

# 在加密后，我们可能会得到一些特殊的值，所以为了避免网络传输中，一些数据存在歧义，用编码封装
base_encrypt_data = base64.b64encode(encrypt_data).decode()
print(base_encrypt_data)    # LTq7K749guf+gGzLJkVQ3g==