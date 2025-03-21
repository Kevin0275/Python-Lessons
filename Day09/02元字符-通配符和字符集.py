import re

# 1. 通配符：.   匹配1个除了换行符\n以外的所有字符
s1 = 'apple ape agree age amazing animate advertise a\ne'

# 找到以a开头，以e结尾，中间有两个非换行符的字符：
res = re.findall('a..e', s1)
print(res)

# 2. 字符集 []：只能匹配一个字符
s2 = 'apple ape agree age amazing animate advertise a\ne a&e a@e a6e a9e'

# 和上面一样，找一个以a开头，以e结尾，中间有一个非换行符的字符

res = re.findall('a.e',s2)
print(res)  # 结果：['ape', 'age', 'ate', 'a&e', 'a@e', 'a6e', 'a9e']

# 如果我想要中间的字符只是英文字母

res_latter = re.findall('a[a-zA-Z]e',s2)
print(res_latter)   # 结果：['ape', 'age', 'ate']

res_latter2 = re.findall('a[^0-9a-zA-Z]e',s2) # ^表示除了这个中括号里面的，也就是取反！
print(res_latter2)  # 结果：['a\ne', 'a&e', 'a@e']