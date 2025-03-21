# 网址：https://www.eastmoney.com/

import requests

url = 'https://www.eastmoney.com/'

res = requests.get(url)
res.encoding = 'utf-8'
print(res.text)

# with open('东方财富.html', 'wb') as f:
#     f.write(res.content)

# print(res.text)

