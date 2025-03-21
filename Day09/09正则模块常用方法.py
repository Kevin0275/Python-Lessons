import re

# [1] search：归根结底，和findall差不多但是它只返回查找到的第一个对象并且返回一个match对象，这个match对象封装了一些信息
# 如果找不到，返回None，而findall如果找不到，返回一个空列表

# 用logs.log文件做一个例子

with open('logs.log', 'r') as f:
    log_text = f.read()
    # print(repr(log_text))

# (1) 查询所有的ERROR：
res_all_error = re.findall('ERROR:.*', log_text)
# print(res_all_error)    #['ERROR: Could not connect to database', 'ERROR: File not found']

# (2) 查询第一个ERROR：
res_first_error = re.search('ERROR:.*', log_text)
print(res_first_error)  # <re.Match object; span=(21, 57), match='ERROR: Could not connect to database'> MATCH对象

# 具体位置：开始和结束
print(res_first_error.span())  # (21, 57)

# 内容：
print(res_first_error.group())  # ERROR: Could not connect to database

# 带分组的案例：
text = '''
服务器的IP地址如下：
主服务器：192.168.1.1
备用服务器：10.0.0.5
外部服务器：172.16.254.1
无效IP：256.100.50.25
外部服务器：192.168.1.256
'''

# 现在我想要第一个外部服务器的IPV4地址：
# res = re.search(r'(?:\d{1,3}\.){3}\d{1,3}',text)  # <re.Match object; span=(18, 29), match='192.168.1.1'> 第一个地址
# res = re.search(r'外部服务器：(?:\d{1,3}\.){3}\d{1,3}',text)  # <re.Match object; span=(45, 63), match='外部服务器：172.16.254.1'> 结果带有外部服务器字样
res = re.search(r'外部服务器：\b(?P<outer_ip>(?:\d{1,3}\.){3}\d{1,3})\b', text)  # 172.16.254.1
print(res.group('outer_ip'))

# [2] match：在search的基础上增加了一个^，也就是匹配开头
res = re.match(r'外部服务器：\b(?P<outer_ip>(?:\d{1,3}\.){3}\d{1,3})\b', text)  # None
# res = re.search(r'^外部服务器：\b(?P<outer_ip>(?:\d{1,3}\.){3}\d{1,3})\b',text)    # 172.16.254.1
print(res)

# [3] split：分割

# python内置有split函数
name = 'Kevin john Smith Jack'
print(name.split(' '))  # ['Kevin', 'john', 'Smith', 'Jack']

name1 = 'Kevin john   Smith      Jack'
res = re.split(r'\s+', name)  # ['Kevin', 'john', 'Smith', 'Jack']
print(res)


# [4] sub 和 subn：替换
text = 'my          name     is         kevin'
# 我希望将所有的空格都换成一个

res_text = re.sub(r'\s+', ' ', text)    # 其实还有第四个参数，就是做多少次替换，不写默认全部替换
print(res_text)

# [5] compile：构建一个正则规则对象
# 由于可能一个规则要使用很多遍，每次都用re库构建表达式再匹配有些麻烦，所以我们使用的是先构建一个对象，然后用它来做正则的匹配

s = '15100649928,123@qq.com,+8613657287791,666@163.com'

# 手机号：以1开头，第二位大于等于3，其余9位不限

res = re.findall(r'(?:\+86)?1[3-9]\d{9}', s)
print(res)

# 用compile：
rule = re.compile(r'(?:\+86)?1[3-9]\d{9}')
res = rule.findall(s)
print(res)


