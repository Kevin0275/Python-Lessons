import json

# 引入一个数据
data = {
    'name': 'Kevin',
    'age': 22
}

# 如果我们使用Python对它进行json格式化
json_data = json.dumps(data)
print(repr(json_data))      # repr函数会将字符串中的转义字符显示出来

'''
这里我们会得到：
'{"name": "Kevin", "age": 22}'      //来自Python的json格式

然而，相同的数据在浏览器的Console打印，得到的是：
JSON.stringfy(data)->
'{"name":"Kevin","age":22}'     //来自浏览器的json格式

很明显，这两个json字符串中具有明显的差别，python版本的多了一些空格，这会导致这两个数据完全不同！

'''

# 解决办法：使用dumps函数中的separator参数，设置元素与元素还有键与值之间的分隔符。

json_data1 = json.dumps(data, separators=(',', ':'))
print(repr(json_data1))

# 现在我们就得到了和浏览器使用的json格式一样的数据字符串：'{"name":"Kevin","age":22}'

# 主要在使用python组装json数据并且发送给服务器的时候需要用到
