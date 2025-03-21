import re

path1 = '/aaa/bbb/blog/2024/12/xxx/yyy/zzz'
path2 = '/blog/2024/12/'

# 如果我们希望就是格式：/blog/年/月/
res1 = re.findall('/blog/[0-9]{4}/[0-9]{1,2}/',path1)
res2 = re.findall('/blog/[0-9]{4}/[0-9]{1,2}/',path2)

print(res1)     # 结果：['/blog/2024/12/']
print(res2)     # 结果：['/blog/2024/12/']

'''
我们会发现两个返回值是一样的，因为正则只需要你字符串中间有匹配的地方就可以

但是有的时候我们希望限制一下这个字符串，控制字符串中严格按照我的规则，不需在两边加上各种乱七八糟的东西

使用^来限制开头，这个字符串的开头必须和我的规则一样
使用$来限制结尾，同上
'''

path_start = '/aaa/bbb/blog/2024/12/'
path_end = '/blog/2024/12/xxx/yyy/zzz'

res_start = re.findall('^/blog/[0-9]{4}/[0-9]{1,2}/',path_start)
res_end = re.findall('/blog/[0-9]{4}/[0-9]{1,2}/$',path_end)

print(res_start, res_end)       # 结果：[] []


res_correct = re.findall('^/blog/[0-9]{4}/[0-9]{1,2}/$',path2)
print(res_correct)      # 结果：['/blog/2024/12/']
