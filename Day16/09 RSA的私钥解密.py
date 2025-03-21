import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

b64_encrypted_data = 'KYZ+KL2kmYph0L17zOaohSugtzEK5xA6eXFw14hhKIhIk9NfLc8KeXQmk24f9fWElhjjm+Y+flRIKafQoW6tmS7ys5WO9uNGhtI/Q6+CjYtLIWjNAPGVjQGc0dToRfgyFZ3gjswcDLXuZTOT/lSXLo2klmxM00xvq8rSmnyAzLg='

# 解开 b64
encrypted_data = base64.b64decode(b64_encrypted_data)

# 数据解密

# 读取私钥
with open('rsa.private.pem') as f:
# 1. 拿私钥
    private_key_str = f.read()
# 2. 构建私钥对象
private_key_obj = RSA.importKey(private_key_str)
# 3. 构建RSA对象
rsa = PKCS1_v1_5.new(private_key_obj)

# 解密
data = rsa.decrypt(encrypted_data, None).decode('utf-8')
print(data)
