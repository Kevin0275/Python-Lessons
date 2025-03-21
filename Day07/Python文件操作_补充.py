
# （1）
# wb 和 w
# ab 和 a    （append）

# w是覆盖写，a是追加写

# f = open('Test','w',encoding='utf-8')
# f.write('hello')    # 如果运行，Text文件里面只剩一句hello

# f = open('Test','a',encoding='utf-8')
# f.write('hello')    # 如果运行，Text文件里面会在最后的结尾加上一句hello

# （2）close 和 with 语句

f = open('Test','a',encoding='utf-8')
f.close()

# close 语句在短的程序里面可能不会有问题，但是如果存在并发程序使用同一个资源，会有bug

# 常见：数据文件，数据库，socket

# 为防止遗忘close：with
with open('Test.txt','w',encoding='utf-8') as f:
    ...
# 自动close

