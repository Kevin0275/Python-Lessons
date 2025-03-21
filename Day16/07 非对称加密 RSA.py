from Crypto.PublicKey import RSA

'''
首先，非对称性加密意味着我们有两套不同的key：公钥和私钥

公钥和私钥是有一定关系的，并不是随便决定的

(1) 公钥加密，私钥解密：数据加密（保护数据）
   A将公钥发给所有人，人手一把，A自己留有一把公钥和一把私钥
   B要给A写信，利用A给的公钥对信件内容进行加密，发给A
   这封加密的信件，只有A自己的私钥可以解开

(2) 私钥加密，公钥解密：数字签名（证明身份）
    A要给B回信，这封信的内容并不怕别人看见，但是A比较担心有人篡改信件内容
    A在写完信后，利用这封信的内容，生成了一个MD5值；
    然后，利用自己的私钥对这个MD5值进行了加密(Signature)，直接放在信件末尾
    B在拿到信之后，可以在读完信后，利用公钥对这个签名进行了解密，并且对比MD5值，
    就知道这封信的确来自于A并且内容正确完整。
'''

# 生成公钥和私钥

# (1) 创建一个对象来生成
rsa_obj = RSA.generate(1024)  # 限制长度 1024

# (2) 导出公钥和私钥
private_key = rsa_obj.exportKey()
public_key = rsa_obj.public_key().exportKey()

with open('rsa.public.pem', 'wb') as f:
    f.write(public_key)
with open('rsa.private.pem', 'wb') as f:
    f.write(private_key)
