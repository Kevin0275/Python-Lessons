import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

base_encrypt_data = 'LTq7K749guf+gGzLJkVQ3g=='

# (1) 去壳，转成encrypt_data
encrypt_data = base64.b64decode(base_encrypt_data.encode())
print(encrypt_data)  # b'-:\xbb+\xbe=\x82\xe7\xfe\x80l\xcb&EP\xde'

# (2) 解密：我们需要知道：算法，key，iv（如果有）

key = '1234567890123456'.encode()
iv = 'asdfghjklzxcvbnm'.encode()
aes_obj = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)

data = aes_obj.decrypt(encrypt_data)
data_unpad = unpad(data, 16)
print(data_unpad.decode())
