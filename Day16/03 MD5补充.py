from hashlib import md5

md5_obj = md5()

data = '123456'.encode('utf-8')

md5_obj.update(data)

hexdigest = md5_obj.hexdigest()     # 拿到的是字符串
digest = md5_obj.digest()   # 拿到的是字节

# 判别 MD5：

'''
1. 字符，a-f，0-9
2. 长度，16x倍数
3. 直接找到接口，用一个常用值，比如123456验证
'''