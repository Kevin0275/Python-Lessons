# 代理就是让代理服务器用不同的ip向服务器发起请求，而不是只用我们自己的电脑的IP
# 代理分为：透明（知道你使用了代理和你的IP），匿名（知道你使用了代理），高匿（推荐）

import requests

# 对这个url发送请求会返回我们的ip地址

url = 'https://qifu-api.baidubce.com/ip/local/geo/v1/district'

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://www.baidu.com',
    'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=68018901_16_pg&wd=ip%E6%9F%A5%E8%AF%A2&fenlei=256&rsv_pq=0xcac6eeed001b558d&rsv_t=fb8aY5muTloLWE4M8l%2FrIok8j1Q4tkQZSxNbcUT5c25Cb6chxK81MgwTsKnl&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=10&rsv_sug1=9&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=ip%25E6%259F%25A5%25E8%25AF%25A2&rsp=5&inputT=3596&rsv_sug4=3596',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = ''

# 创建代理池：
proxy = {
    'https': 'xxx.xxx.xxx.xxx:xxxx'
}

response = requests.get(url, params=params, headers=headers, proxies=proxy)

print(response.json().get('ip'))