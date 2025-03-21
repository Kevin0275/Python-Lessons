from hashlib import md5

# (1) MD5 实例化

md5_obj = md5()

'''
作为摘要算法，MD5 和普通的加密算法不一样，加密算法可以加密也可以解密，但是摘要算法过程不可逆
MD5 产出的字符串固定为 32 位，并且一般由 a-f，0-9 组成
相同的参数产出结果一样，但是，不同的参数的结果千差万别
'''

# (2) update 更新数据：做摘要

md5_obj.update('hello world'.encode('utf-8'))   # 注意：传入的应该是字节
# 没有返回值，我们提取需要进行下一步的操作

# (3) 提取摘要值
ret = md5_obj.hexdigest()   # 5eb63bbbe01eeed093cb22bb8f5acdc3
# ret1 = md5_obj.digest()
print(ret)

# 有的时候一些简单的 MD5 会被 “撞库” 破解，也就是用一个数据库去撞密码
# 为了避免这件事，我们采用加盐！

salt = b'fjisanfodsbfihe'   # 一个服务器提供的复杂字符串
md5_obj1 = md5(salt)

md5_obj1.update('hello world'.encode())
print(md5_obj1.hexdigest())     # 9924ecbdc968f181339c43eec70416c5  完全不一样而且极难破解

# 对于一个MD5对象，如果我们多次update数据，那么随后hexdigest得到的结果是这一堆字符串拼接后的结果

# MD5 还可以用于验证一致性，因为文件在传输的过程中会存在一些可能的数据丢失，所以比较MD5值是解决这个问题的一个方法
