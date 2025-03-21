# 网站：http://www.kfc.com.cn/kfccda/storelist/index.aspx

import requests
import time

page_number = int(input('请问你要多少页的餐厅数据：')) + 1

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
for i in range(1,page_number):
    my_data = {
        'op': 'cname',
        'cname': '北京',
        'pid': '',
        'pageIndex': i,
        'pageSize': '10',
    }

    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
    }

    res = requests.post(url, data=my_data).json()

    restaurant_list = res.get('Table1')

    # print(restaurant_list)

    for restaurant_dic in restaurant_list:
        address = restaurant_dic.get('addressDetail')
        info = restaurant_dic.get('pro')
        print(address, info)
    time.sleep(2)
