# 网址：https://www.icve.com.cn/
import json

import requests

# 爬取：合作院校

url = 'https://www.icve.com.cn/portal/portal/getSchoolList'

page_number_str = input('请问你要爬取多少页的数据：')

page_number = int(page_number_str) + 1  # 方便for循环

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'referer': 'https://www.icve.com.cn/'
}
for j in range(page_number):
    my_data = {
        'page': j
    }

    res = requests.post(url, headers=my_headers, data=my_data)

    res_json = res.json()

    school_list_json = res_json.get('list')

    school_list = json.loads(school_list_json)

    for school in school_list:
        print(school.get('Name'))

# 错误的：
# res_json = json.loads(res.text)
# school_list_json = res_json.get('list')
# school_list = school_list_json.json() # 不能用，因为x.json()是requests库自带的函数，只用于解析response的json格式
# print(school_list_json)
# print(type(school_list))
