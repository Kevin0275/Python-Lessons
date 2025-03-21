# 反斜杠
# path = 'C:\next\table\paper.txt'
# 这里的反斜杠由于 \n 是换行符，\t 是缩进符，路径编译会出现错误。

# 解决方法：
# 1：
# path1 = 'C:\\next\\table\paper.txt'  # 使用双反斜杠来取消特殊含义。
# 2：
# path2 = r'C:\next\table\paper.txt'  # 使用Pycharm特有的取消反斜杠特殊含义的 r.

# print(path, path1, path2)

# 格式化输出：可以在既定字符串中改变特定位置的值。
# Introduce = 'My name is Karrigan, and my age is 32.'

# 如果我们希望改变名字和对应的年龄，那么我们需要在这个字符串加入变量。

# 设定变量
# name = input('Enter your name: ')
# age = input('Enter your age: ')

# 在字符串中引入变量
# Introduce1 = 'My name is %s, and my age is %s.' % (name, age)
# Introduce2 = f'My name is {name}, and my age is {age}.'

# 第二种方式更为常用因为更加简洁，第二种方式适用于Python 3.6及以后的版本。

# 字符串的一些内置方法。
# s = 'How old are you?'
# 注意：字符串是一种不可变类型。

# [1] 转大写
# s1 = s.upper() # upper函数会生成一个基于s的新的字符串，原来的s并不会被改变因为我们并没有对它重新赋值。
# 转小写
# s2 = s.lower()

# [2] 判断开头和结尾（生成bool值）
# s3 = s.startswith('M') # False.
# s4 = s.endswith('?') # True.

# [3] strip去除字符串两端的空格和换行符。
# string1 = '       what is it?        \n'
# string2 = string1.strip()
# print(string2)

# [4] split将字符串切片，并且改变为字典形式
# s = 'London NewYork Beijing Paris'
# s_dic = s.split(' ')
# print(s_dic)
# 请注意：这种方法有一定的局限性，元素之间的分隔必须是同一种，空格，逗号等。

# [5] join将一些在字典中散碎的字符串拼接成字符串。
# s1 = ' '.join(s_dic)
# print(s1)

# [6] index and find：查找某个字符
# s = 'Hello World!'

# 两种内置方法在找寻结果为 True 时，返回结果相同。返回结果是第一个关键字符出现的索引位置。
# s_1 = s.index('Hello')
# print(s_1)
# s_2 = s.find('World')
# print(s_2)

# 出现区别是在找寻结果为 False 时，返回结果不同。
# s1 = s.index('world')   # 返回结果显示，ValueError: substring not found
# s2 = s.find('world')    # 返回结果显示：-1，不报错
# print(s1)
# print(s2)

# [7] replace：替换字符串中的某个字符
# s = 'Hello World!'
# s1 = s.replace('World', 'Python')
# print(s1)
