import re

# 重复符有四种：{}，*，+，?

s = 'aeeee apple acre ape agree age amaze animate advertise a\ne a&e a@e a6e a9e'

# 如果要查找以a开头以e结尾的中间两个非换行符的字符：
res_a2e = re.findall('a..e', s)
print(res_a2e)  # ['aeee', 'acre', 'agre', 'adve']

# 当然，也可以使用重复符 {} ：表示重复符号左边的重复几次
res_a2e_first = re.findall('a.{2}e', s)
print(res_a2e_first)  # ['aeee', 'acre', 'agre', 'adve']

# 更常用的是：使用范围
res_a2e_second = re.findall('a.{1,3}e', s)  # 代表a和e之间可以存在1，2，3个字符
print(
    res_a2e_second)  # ['aeeee', 'apple', 'acre', 'ape', 'agree', 'age', 'amaze', 'ate', 'adve', 'a&e', 'a@e', 'a6e', 'a9e']
# 但是存在一个问题，因为1，2，3个字符都可以，所以理论上来说对于字符'aeeee'有一些模糊不清的地方

# 贪婪匹配：当一段字符有多种选取情况符合要求，按照最大允许范围内的匹配数量进行匹配，默认进行贪婪匹配
# 取消贪婪匹配：在重复符后面跟一个?
res_a2e_third = re.findall('a.{2,3}?e', s)
print(res_a2e_third)  # ['aeee', 'apple', 'acre', 'agre', 'amaze', 'adve']

# {}的两个数可以留空一个，也就是无穷或极小
res_a2e_forth = re.findall('a.{2,}e', s)
print(res_a2e_forth)  # ['aeeee apple acre ape agree age amaze animate advertise', 'a&e a@e a6e a9e']

# 如果我们需要让通配符 . 强行匹配任意符号，也包含换行符，那么我们就需要使用第三个参数，也就是模式切换
res_a2e_all = re.findall('a.{2,}e', s, re.S)
print(res_a2e_all)  # ['aeeee apple acre ape agree age amaze animate advertise a\ne a&e a@e a6e a9e']

s1 = "a\re a\ne"
res = re.findall(r'a[^\n]e', s1)
print(res)  # 返回 ['a\re']，所以在这里所有转义符按照一个符号处理

'''
其余三种重复符是对于第一种也就是{}的化简：
* = {0,}
+ = {1,}
? = {0,1}

请注意，?不一定只有取消贪婪匹配的作用，就像^也不一定只有反选的作用一样，具体的还是要看位置
'''

# 请找出下列字符串中的网址：
url = 'https://baidu.com kevin https://jd.comjohnhttp://taobao.com'
url_find = re.findall('https?://[a-zA-Z]*?.com',url)
print(url_find)

