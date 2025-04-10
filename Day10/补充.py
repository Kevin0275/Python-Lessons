# 关于__name__

print(__name__)
# 返回 __main__

'''
__name__是python自己的一个变量，它标注了运行的程序是否是启动项
也就是说，如果我们运行这个叫做'补充.py'的文件，那么他就是启动文件，返回的值也就是__main__

但是如果我们用另外一个文件，import 补充.py，那样的话，我们就会看到打印出来的应该是文件名而不是main

这个功能经常在做测试的时候被使用，因为我们并不想让别人看到我们的测试内容

注意：import的时候我们会把文件执行一遍再导入
'''
