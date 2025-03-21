# session其实就是比requests具有自动保存和自动管理cookie的功能

# 还是雪球网

import requests

# 创建一个session对象
session = requests.session()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=1a0c66d417365153926958973e004c078a2c7e82009457e21decf11dad8a4d',
    'Referer': 'https://xueqiu.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'md5__1038': 'QqGxcDnDyiitnD05o4+r=D97fIrqiKDCDrjeD',
}

# 访问主网站（第一次访问）
session.get('https://xueqiu.com/', headers=headers, params=params)

# 直接拿ajax

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://xueqiu.com/S/BABA?md5__1038=n4jhYKBKD5iKY5DsD7%2B30Qei%3D56U1Cli7oD',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'elastic-apm-traceparent': '00-95113478a94955cdaaadf9c165ae9732-0ab67deb97170ef6-00',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'code': 'BABA',
    'type': '1',
    'size': '100',
    'md5__1038': 'n4mhDIqfgGCFDs5YYK0=GOD9AA3PD=+G=a4D',
}

res = session.get('https://xueqiu.com/stock/industry/stockList.json', headers=headers, params=params)
print(res.text)