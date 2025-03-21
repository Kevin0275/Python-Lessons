# 网址：https://www.xiachufang.com/search

import os
import time

import requests

url = 'https://www.xiachufang.com/search'

menu = input('请输入你想查询的菜品：')
os.makedirs(f'下厨房爬取/{menu}', exist_ok=True)

page_number = int(input('请输入你要查询多少页的信息：'))

for i in range(1, page_number + 1):
    my_params = {
        'keyword': menu,
        'cat': '1001',
        'page': i
    }

    res = requests.get(url, params=my_params)

    # print(type(res.content))

    with open(f'下厨房爬取/{menu}/{menu}_第{i}页.html', 'wb') as f:
        f.write(res.content)
    time.sleep(3)

print('你要求的菜谱已经下载完毕！')

# print(res.text)
