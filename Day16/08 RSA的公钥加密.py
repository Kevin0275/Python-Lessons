from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

data = 'Hello World!'

# 拿公钥
with open('rsa.public.pem', 'rb') as f:
    # 1. 获取公钥
    publicKeyStr = f.read()
    # print('Public key:', publicKeyStr)
    # 2. 基于公钥生成公钥对象
    public_key_obj = RSA.importKey(publicKeyStr)
    # 3. 基于公钥对象生成RSA算法对象
    rsa_public_key = PKCS1_v1_5.new(public_key_obj)

# 数据加密
encrypted_data = rsa_public_key.encrypt(data.encode())
# print(encrypted_data)
b64_encrypted_data = base64.b64encode(encrypted_data)
print(b64_encrypted_data.decode())
