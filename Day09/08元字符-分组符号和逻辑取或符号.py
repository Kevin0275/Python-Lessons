# 分组符号（也有优先提取功能） ()
# 逻辑取或关系 |
import re

s = 'apple banana orange aaa appleappleapple appleapple'

# 如果我想要'aaa'，那么很简单：
res_aaa = re.findall('aaa',s)
print(res_aaa)   # 结果：['aaa']

# 如果我想要'apple'重复两次或者三次的，就需要将apple这个词重复两次或者三次：
# res_apple = re.findall('apple{2,3}',s)  # 请注意这是不可以的，因为{2}只允许把e重复而不是apple
res_apple = re.findall('(?:apple){2,3}',s)  # 优先提取，一会说
print(res_apple)       # 结果：['appleappleapple', 'appleapple']


text = '''
Visit us at user@qq.com for more info.
Contact support at support@qq.com.
Also, check out admin@my163.com and info@163.com
Besides, we have an email for you: kevin@hotmail.cn
'''

# 目标：提取所有域名为结尾有163的
res_163 = re.findall(r'\b[\w.-]+@\w*163\.com\b',text)
print(res_163)      # ['admin@my163.com', 'info@163.com']

# 如果这次我只想要邮箱名而不用带有后缀，那么我们可以考虑使用()的优先提取功能
res_163_1 = re.findall(r'\b([\w.-]+)@\w*163\.com\b',text)
print(res_163_1)    # ['admin', 'info']

# 如果这次我要.com或者.cn结尾的所有邮箱：
pattern = r'\b\w*@[\w.]*com|\w*@[\w.]*cn\b'
print(re.findall(pattern,text))     # 结果：['user@qq.com', 'support@qq.com', 'admin@my163.com', 'info@163.com', 'kevin@hotmail.cn']

# 如果我们只需要对于一部分进行分组，其他的不变，那么没必要写的这么麻烦
pattern2 = r'\b\w*@[\w.]*(com|cn)\b'    # 结果：['com', 'com', 'com', 'com', 'cn']，优先提取
pattern3 = r'\b\w*@[\w.]*(?:com|cn)\b'  # 结果：['user@qq.com', 'support@qq.com', 'admin@my163.com', 'info@163.com', 'kevin@hotmail.cn']
print(re.findall(pattern3,text))
