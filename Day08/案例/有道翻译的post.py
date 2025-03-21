# 网址：https://ai.youdao.com/product-fanyi-text.s
import requests

origin = input('Please input the words or sentences you want to search:')

url = 'https://aidemo.youdao.com/trans'

my_data = {
    'q': origin,
    'from': 'Auto',
    'to': 'Auto'
}

res = requests.post(url, data = my_data)    # 请求头Content-Type：application/x-www-form-urlencoded; charset=UTF-8

# 响应是json数据，所以我们用
# print(res.json())

res_json = res.json()

# 如果只提取一项：
print(res_json.get('translation')[0])

