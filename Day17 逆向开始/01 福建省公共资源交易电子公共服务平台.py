import base64
from Crypto.Cipher import AES
import requests
import json
from Crypto.Util.Padding import pad, unpad

# 方法关键字：在源数据里面，全局搜索decrypt(，因为web这边肯定做了解密

# 搜索到如果存在这样一个函数，那么接下来我们应该判断是不是这个接口的确对于我们的目标数据做了解密：断点测试

# 测试到了我们需要的函数接口之后：逆向
def decrypt(response):
    # (1) base64 解码
    b64_encrypted_data = response.json().get('Data')
    encrypted_data = base64.b64decode(b64_encrypted_data)
    # (2) 解密
    key = '0124563789123456'.encode()
    iv = encrypted_data[:16]
    # !!!这两个值随便取的，但是真的实操自己去分析文件拿数据

    aes_obj = AES.new(key=key,mode=AES.MODE_CBC,iv=iv)

    data = aes_obj.decrypt(encrypted_data)

    new_data = unpad(data,16)

    data_text = new_data.decode()

    return data_text

def main():
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

    # ！！！！
    '''
    因为爬虫要批量爬取数据，有的时候我们会发现，pageSize这个参数不能是4，不能是6，只能是5
    所以，for 循环失效!!!
    
    原因：为了防止爬虫，开发人员会在本地部署一系列的 JS 文件，在发送请求之前，根据自己的载荷，计算出一个 sign 值，与请求一同发送
    服务器端也会根据这个sign值拆解，算法不定：摘要或者加密都可以（类似于数字签名）
    
    有意思的是：在这个JS文件里面搜索 encrypt 的时候，断点显示并不是我们要找的，所以关键字搜索失效了
    
    key 关键字：找标头！
    
    '''

    response = requests.post(url, headers=headers, json=json_data)

    # print(response.text)

    return decrypt(response)

if __name__ == '__main__':
    main()


# 截止到现在我们所做的其实都是在分析JS代码，找到逻辑，并且用python模拟实现，但是当JS文件增多，这样的方式比较麻烦，所以我们采用JS逆向

