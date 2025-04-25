import requests
import json

url = 'https://m.douban.com/rexxar/api/v2/movie/recommend/'

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'referer': 'https://movie.douban.com/explore'
}

tags = input('输入你想看的电影类型：')

my_params = {
    'start': 0,
    'count': 60,
    'tags': tags
}

res = requests.get(url=url, headers=my_headers, params=my_params)
print(res.text) # 如果返回的数据是一个页面，就没办法用json来做
print(res.json()) # 如果返回的数据是一个json字符串，就可以用json来做反序列化，这个方法是requests自带的，如果你用json.loads()，就需要你自己导入json模块了
print(json.loads(res.text)) # 当然，这样也行

'''
顺便一提，json.load一般是输入一个文件，然后读取为Python字符串
json.loads()一般是输入一个已经在内存上的json字符串然后转换
'''

# 一般来说，Ajax返回的响应数据都是json字符串，因为需要浏览器用JS去渲染
