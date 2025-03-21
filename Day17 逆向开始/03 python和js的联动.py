import execjs
import requests
import base64

url = 'https://ggzyfw.fj.gov.cn/FwProtalApi/Article/PageList'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'referer': 'https://ggzyfw.fujian.gov.cn/'
}

json_data = {
    'pageSize': 5,
    'type': '12',
    'ts': 1735301931489
}

response = requests.post(url, headers=headers, json=json_data)

b64_encrypted_data = response.json().get('Data')
encrypted_data = base64.b64decode(b64_encrypted_data)

# 构建JS编译器

# 拿到JS代码数据
js_code = open('02 解密数据.js').read()

# 构建编译
js_compile = execjs.compile(js_code)

# 执行，传参     -> 函数调用，参数
data = js_compile.call('b', encrypted_data)
print(data)