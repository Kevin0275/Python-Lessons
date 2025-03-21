import re

# 补充
s1 = 'yuan 23 kevin 19 john 2198 smith 32189321'
# 要所有的数字
res_num = re.findall('[0-9]+', s1)
print(res_num)

# 针对于一个转义符，使用大写字母会有取反义的一个效果

# 第一个转义符：\d，代表[0-9]
# res_trans1 = re.findall('\d+', s)     这样写，python会自动认为反斜杠是python的转义，可能以后有错
res_trans1 = re.findall(r'\d+', s1)
print(res_trans1)

s2 = 'yuan 23 kevin 19 john 2198 smith 32189321 abb90s'

# 要所有的名字
res_name= re.findall('[a-zA-Z]+', s2)
print(res_name)     # 结果：['yuan', 'kevin', 'john', 'smith', 'abb', 's']

# 第二个转义符：\w，代表[a-zA-Z0-9_]，所有字母加数字加下划线
res_trans2 = re.findall(r'\w+',s2)
print(res_trans2)

# 第三个转义符：\b
s3 = 'The cat sits on the caterpillar. I love cat! cat2'

# 我想要所有的cat单词
# \b：代表单词的边界，单词包括[0-9a-zA-Z]
res_cat = re.findall(r'cat\b',s3)
print(res_cat)  # 结果：['cat', 'cat']

'''
The cat 中的cat被提取出来
caterpillar 中的cat不会被提取出来因为e不算边界
cat! 中的cat会被提取出来因为!算是边界
cat2 中的cat不会被提取出来因为2不算边界
'''

# 第四个：\s 匹配的是一个空白符，可以是空格，换行，制表等等

# 第二个功能：取消特殊符号的意义
url = 'https://wwwxlufei.com/https://www.baidu.com/ kevin https://www.jd.com/johnhttp://www.taobao.com/'
# 如果我要所有的网址：
# url_find = re.findall('https?://www.[a-z]*.com/',url)
'''
你会发现在这里面我们的www.中的 . 和正则里面的通配符完全一致，但是我们在这里并不想要https://wwwxlufei.com/
所以我们取消这两个点的特殊意义
'''

url_find = re.findall(r'https?://www\.[a-z]*\.com/',url)

print(url_find)


path = r'C:\kevin\document.txt D:\kevin\file.txt E:\kevin\assignment.txt fiosajeirnowa'
# 要所有的路径

res_path = re.findall(r'\w:\\kevin\\\w+\.txt',path)
print(res_path)     # 结果：['C:\\kevin\\document.txt', 'D:\\kevin\\file.txt', 'E:\\kevin\\assignment.txt']

# 其实没有必要特意“避免”双斜杠，因为它仅仅是 Python 输出字符串的表现形式。当你真正使用这些路径时，它们已经是带单斜杠的路径。
# 只是因为：当 Python 输出字符串时，它会对反斜杠进行转义，导致它看起来像是双斜杠

