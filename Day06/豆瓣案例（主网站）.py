import requests
import json

url = 'https://movie.douban.com/'
my_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
response = requests.get(url=url, headers=my_headers)
print(response.text)
print(type(response.content))
with open('Douban.html','wb') as f:
    f.write(response.content)