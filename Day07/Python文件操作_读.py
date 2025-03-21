# 打开或者创建一个文件

# 读模式：r是读字符，rb是读字节

# 读字符
# 返回一个句柄
# f = open('Test', mode='r', encoding='utf-8')
# 请注意，这里操作系统会去磁盘上读取字节并且decode，MAC默认使用UTF-8，WIN默认GBK

# data = f.read()  # 慎用，将所有数据读到内存中
# print(data)

# 读指定长度
# limited_interval_data = open('Test', mode='r', encoding='utf-8')
# data = limited_interval_data.read(1)

# 读整个文件，循环遍历

# f = open('Test', mode='r', encoding='utf-8')
# for line in f:
# print(line, end='')

# 读文件字节
f = open('Test', mode='rb')
data = f.read()
print(data)

# 读img文件
img_f = open('Test_img.jpg', 'rb')
data_img = img_f.read()
print(data_img)




