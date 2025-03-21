import urllib.parse

# 主要用来做网络传输

# （1）url 的值编码

a = 'kevin'

res_a = urllib.parse.quote(a)
print(res_a)  # kevin，因为里面没有特殊符号

b = 'kevin 李'

res_b = urllib.parse.quote(b)
print(res_b)  # kevin%20%E6%9D%8E

# 解码
a1 = urllib.parse.unquote(res_a)
print(a1)

b1 = urllib.parse.unquote(res_b)
print(b1)

# （2）对字典做一个整体的一个url编码

data = {
    'name': 'kevin 李',
    'pwd': '123'
}

# 对字典进行编码
url_data = urllib.parse.urlencode(data)
print(url_data)  # name=kevin+%E6%9D%8E&pwd=123

# 解码
url_origin = urllib.parse.parse_qs(url_data)
print(url_origin)  # {'name': ['kevin 李'], 'pwd': ['123']}

# 由于在url里面可能一个key对应多个value，所以它自动把value处理成列表格式
# 可以用字典推导式来解开列表格式

url_unlist = {key: value[0] for key, value in url_origin.items()}
