from hashlib import md5,sha256,sha1,sha224


# 一些对象创建
md5_obj = md5()     # len = 32
sha1_obj = sha1()   # len = 40
sha224_obj = sha224()   # len = 56
sha256_obj = sha256()   # len = 64

data = '123456'.encode('utf-8')

md5_obj.update(data)
sha1_obj.update(data)
sha224_obj.update(data)
sha256_obj.update(data)

print(md5_obj.hexdigest(), len(md5_obj.hexdigest()))
print(sha1_obj.hexdigest(), len(sha1_obj.hexdigest()))
print(sha224_obj.hexdigest(), len(sha224_obj.hexdigest()))
print(sha256_obj.hexdigest(), len(sha256_obj.hexdigest()))

