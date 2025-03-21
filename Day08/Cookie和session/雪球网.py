# 网址：https://stock.xueqiu.com/v5/stock/portfolio/list.json
# 由于cookie是可变的，我们接下来看一看怎么通过requests来获得cookie

# import requests

# cookies = {
#     'cookiesu': '471736513238635',
#     'device_id': 'a33dd607adae5549852a3991cafeee1d',
#     'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1736513239',
#     'HMACCOUNT': '2DE0B3929D3B8070',
#     'is_overseas': '0',
#     'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1736513841',
#     'remember': '1',
#     'xq_a_token': 'c470ce9d35f5fa67d4e82c50fb4d2c3f17a97226',
#     'xqat': 'c470ce9d35f5fa67d4e82c50fb4d2c3f17a97226',
#     'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjc2MDY4ODYwODQsImlzcyI6InVjIiwiZXhwIjoxNzM5MTA1ODgzLCJjdG0iOjE3MzY1MTM4ODMzMDQsImNpZCI6ImQ5ZDBuNEFadXAifQ.I8E21eJ7QI_pNVKv8A2NBJm1I7Z2gs2oh1ehxRNQ-hmM4iws2o33Cadp7yN_ZH91H-Au74d5U0aCLUKaaD8jEIQbgxIJaFSHBFHUwHf76V837cJRs4ASWWFo4yX6yrNzke--tqOHWlewBk-P1u4_b6JUQmndJ3CMERYIx0v_NtZMi3qfcvaEEb9sPXBf8sjFkqvmB9XFA7VguD3GaSwxIJvcrQGnGZiwZHd2HeRAxGTQpK0pC-Tlbi693CfUxzQ1ladcy3Zs7Wy_z6maZK4TaHufl67fjR3h7VBQFZUf3eOF4nbOrHrr1pJ-KV5Qn1M7Nn3ihvVNYPSMoG1X3gblpg',
#     'xq_r_token': 'c177aa338802d5c468900a76575c6b86f2a68266',
#     'xq_is_login': '1',
#     'u': '7606886084',
#     'ssxmod_itna': 'YqGx9DgDyDuD2Dfx2Dz=DUiUqfLOGC7D0xxGKW+UtD/+ADnqD=GFDK40o38urc+xiYDx4dhaliixdeKYB4nDFQG7GcTatADB3DEx0=KC3ixiiBDCeDIDWeDiDG4tDFxYoDeaXQDFCT5XzUhKDpxGrDlKDRx07qSKDbxDaDGpkQAexUPOHUEKDhxDCDiyhG3YDixia2rDDBrDjeQGoprDDEB911pBGd33qygGqUxG1DQ5DsxxRO48RdTisyxj09R485zYDvxDktFyHdzrCVpHO98hojQdPVQ4PPo+qp74xQ7GoF7G4=7+5t0xYQDqee5BetApjnUTE+jYD===',
#     'ssxmod_itna2': 'YqGx9DgDyDuD2Dfx2Dz=DUiUqfLOGC7D0xxGKW+tG9FoDBkP7Q7GcDewiD==',
# }
#
# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     # 'cookie': 'cookiesu=471736513238635; device_id=a33dd607adae5549852a3991cafeee1d; Hm_lvt_1db88642e346389874251b5a1eded6e3=1736513239; HMACCOUNT=2DE0B3929D3B8070; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1736513841; remember=1; xq_a_token=c470ce9d35f5fa67d4e82c50fb4d2c3f17a97226; xqat=c470ce9d35f5fa67d4e82c50fb4d2c3f17a97226; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjc2MDY4ODYwODQsImlzcyI6InVjIiwiZXhwIjoxNzM5MTA1ODgzLCJjdG0iOjE3MzY1MTM4ODMzMDQsImNpZCI6ImQ5ZDBuNEFadXAifQ.I8E21eJ7QI_pNVKv8A2NBJm1I7Z2gs2oh1ehxRNQ-hmM4iws2o33Cadp7yN_ZH91H-Au74d5U0aCLUKaaD8jEIQbgxIJaFSHBFHUwHf76V837cJRs4ASWWFo4yX6yrNzke--tqOHWlewBk-P1u4_b6JUQmndJ3CMERYIx0v_NtZMi3qfcvaEEb9sPXBf8sjFkqvmB9XFA7VguD3GaSwxIJvcrQGnGZiwZHd2HeRAxGTQpK0pC-Tlbi693CfUxzQ1ladcy3Zs7Wy_z6maZK4TaHufl67fjR3h7VBQFZUf3eOF4nbOrHrr1pJ-KV5Qn1M7Nn3ihvVNYPSMoG1X3gblpg; xq_r_token=c177aa338802d5c468900a76575c6b86f2a68266; xq_is_login=1; u=7606886084; ssxmod_itna=YqGx9DgDyDuD2Dfx2Dz=DUiUqfLOGC7D0xxGKW+UtD/+ADnqD=GFDK40o38urc+xiYDx4dhaliixdeKYB4nDFQG7GcTatADB3DEx0=KC3ixiiBDCeDIDWeDiDG4tDFxYoDeaXQDFCT5XzUhKDpxGrDlKDRx07qSKDbxDaDGpkQAexUPOHUEKDhxDCDiyhG3YDixia2rDDBrDjeQGoprDDEB911pBGd33qygGqUxG1DQ5DsxxRO48RdTisyxj09R485zYDvxDktFyHdzrCVpHO98hojQdPVQ4PPo+qp74xQ7GoF7G4=7+5t0xYQDqee5BetApjnUTE+jYD===; ssxmod_itna2=YqGx9DgDyDuD2Dfx2Dz=DUiUqfLOGC7D0xxGKW+tG9FoDBkP7Q7GcDewiD==',
#     'origin': 'https://xueqiu.com',
#     'priority': 'u=1, i',
#     'referer': 'https://xueqiu.com/S/SH688256?md5__1038=eqUhGK4mx0rx7YD%2FzR47KG%3DG8KH5it3sF4D',
#     'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
# }
#
# # 在这里cookie是注释掉的，因为cookie是比较重要的一部分而且经常会出问题，我们一般不在headers里面写死这个值，而是用单独的一个cookie
#
# params = {
#     'sytem': 'true',
#     'md5__1632': 'n4+xuDRDBDgDnDGx1DlxEe0=KG=G8t8CRGQ0eD',
# }
#
# response = requests.get('https://stock.xueqiu.com/v5/stock/portfolio/list.json',
#                         params=params,
#                         cookies=cookies,
#                         headers=headers
#                         )
# print(response.text)

# 这次我们模拟第二次发送请求，但是没有cookie，我们需要自己去获得这个cookie，也就是动态cookie
# 这第二次的cookie肯定依赖于第一次访问的cookie和响应cookie，所以我们要发送两套请求，第一套不带cookie，第二套带cookie
# 如果这个服务器设定的cookie是静态的，那么这样很笨，但是如果是动态的，就会很有用！

# 第一次请求（对主网站）
import requests

cookies = {
    'acw_tc': '1a0c66d417365153926958973e004c078a2c7e82009457e21decf11dad8a4d',
}

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

response = requests.get('https://xueqiu.com/', params=params, cookies=cookies, headers=headers)
# 拿到cookie
c1 = response.cookies.get_dict()

# print(cookies)

# 第二次请求（对我想要的ajax）

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

response = requests.get('https://xueqiu.com/stock/industry/stockList.json', params=params, cookies=c1, headers=headers)
print(response.text)