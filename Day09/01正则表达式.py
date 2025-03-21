'''
正则是为了模糊查询复杂文本
'''

import re   # 正则库，python内置

# 找到有没有kevin
s = 'kevin john smith lisa'
print(s.find('kevin'))  # 返回第一个字符的所在索引
# 这个和正则一点关系没有，纯粹是python的内置精准查找

#正则
s = '12 kevin 24 john 129 smith 1293021 lisa'
# 找到所有的数字
num = re.findall(r'\d+', s)  # \d是找到所有十进制数字，+代表不限位
print(num)

# 这个\d+ 是元字符，也就是正则在查找的时候使用的一定查找规范。常用的有11个


