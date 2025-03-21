# 爬虫程序就是将程序模拟成浏览器向服务器发送请求

# 模块和包：模块就是一些代码，random，datetime等等，但是如果代码很多，那可能一个文件放不下，就用包，directory

'''
模块主要分成两类：
1. 标准库
2. 第三方
3. 自定义
'''

import requests
import json

# 基于HTTP协议模拟浏览器向目标服务器发送请求

'''
一个基本的请求包含：
1. URL
2. 请求方式
3. 请求头
4. 载荷
'''

# 抓包百度：https://www.baidu.com

# url的设定
url = 'https://www.baidu.com/'

# 请求头
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'Referer': 'https://www.baidu.com/',
    'Host': 'www.baidu.com'
}
#

my_params = {

}
# params是查询参数，get

my_data = {

}
# data是请求体参数，post

response = requests.get(url=url, headers=my_headers, params=my_params, data=my_data)

# response是响应，可以进行接受来自于服务器的响应，一个响应包含：响应代码，响应头，响应体

print(response.status_code)  # 响应代码
print(response.headers)  # 响应头
print(response.text)  # 响应体

# 注意，text只有在返回数据是一个文本【html、json】，其他例如img，音频就用content（元数据）

# 当然，我们可以用requests相应的发送post请求

res1 = requests.post(url=url, headers=my_headers, data=my_data)

# 我们会获取到相应的由浏览器发送回的响应

'''
值得注意的是：我们在post请求中，会因为请求的请求体的不同格式而需要明确格式：
默认的data是用 url-form 表单格式
当然也可以用以下两种方式发送json格式
'''

# 发送json格式数据方法1：有坑！
res_json = requests.post(url=url, json=my_data)
'''
问题出现在json格式化的字符，由于requests也是用json.dumps来做格式化，空格会出问题！
'''

# 发送json格式数据方法2：推荐
res_json_1 = requests.post(url=url, data=json.dumps(my_data, separators=(',', ':')))

'''
需要提醒的是，由于requests对于这种data的请求参数，一般都是自动补全请求头为form表单格式，但是我们需要的是
json格式，所以不要忘记在请求头的时候带上一行参数，是：
'Content-type':'application/json'
'''




