import base64

# (1) base64 编码
s = 'you'.encode()
ret = base64.b64encode(s).decode()
print(ret)

# (2) base64 解码
ret1 = base64.b64decode(ret)
print(ret1)

# 注意：一般来说，满足 base64 的码都是可以被4整除的码，有的时候补全的等号是可以被删掉的

# 有的时候会有不一样的base64语言，一般来说是为了SQL消除歧义把“+”变成了“-”，“/”变成了_
