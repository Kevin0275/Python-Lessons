import requests

url = 'https://img-cdn.hltv.org/gallerypicture/ru-5waNhj9B8FxkVDj5xrK.jpg'
# print(type(requests.get(url).content))
my_headers = {
    'accept':
    'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-encoding':
    'gzip, deflate, br, zstd',
    'accept-language':
    'zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7',
    'cache-control':
    'no-cache',
    'cookie':
    '_ga=GA1.1.1313385511.1743172824; _fbp=fb.1.1743172823961.837869937865864607; _sharedid=3b1e0f5f-bb43-4c88-83f8-5206d31eb6d3; _pubcid=5c880b49-d890-40cb-822a-2e1859936320; _pubcid_cst=VyxHLMwsHQ%3D%3D; __gads=ID=6f381365d480e7a7:T=1743172924:RT=1745207298:S=ALNI_MavRt2NfWeg9ZHs8wRSkd5kY85b9A; __gpi=UID=00001079069a62f4:T=1743172924:RT=1745207298:S=ALNI_MbrfYZ8P2j5CGLH-4MXD9cEMzaqAQ; __eoi=ID=27ded2b3ac2e19fd:T=1743172924:RT=1745207298:S=AA-AfjZ0XO-pm3hVk6IjPeq_7yj5; __cf_bm=qB03HEWfipprPVVTfh7eWBRj9A2nRAMLHmu9OI49Uco-1745551585-1.0.1.1-1sx.1T5GOfLJcvIZVP5XhY8ft_UpwEQoNugTP_2Ut405s1qpUVqsYYx9oksuIfA768Z.9A3LOb2mhcnGESeYmC7DfaQcEum_8XQW7ZK7PxA; cf_clearance=f9HATUQBy_pH6FTg.ejsT.FyxQrR8Qzhy1z2m_lv0Is-1745551586-1.2.1.1-zWJKHKXc9FExLOvk8dm3EkJKuOXNW57CudiyxOjqYbbvP.56SL_5pV_5.26RJmHIriUMnp41QRkywrBzaaEOEPBGxR1Xcitkgh4U_jXtlbX8cOUkdYCXmF6bTXebK4mw5WB26_vy6jEG.yRf_ATIw3AxsMJrUOZRQvhow67d9scQwrpETmVKhvjf2HhgeWQ4dXfEVvn_IXbWj.kpbxhm7NJuUsWAzKJuFZ_MdimIbRDP8UXWmoU.Bdi84Kfb1pN1CWn09.y.A3offEIXSbrdbp_PhSahgHOetQmAGk5k5ia2yoFgXXZ8ILhW9up7YnbhtxzcInRHrmXS0F.700J280dK6Z_OtlZT3rtz96GwNBg; _sharedid_cst=kSylLAssaw%3D%3D; cto_bundle=XcSFrF9YM0IzTzBzNEprZFI2eXBhZk1VdGtKcmtpd2JaUDBSYnN6Z0Q3ZUFjd05JbGMyNVklMkY4NWZmeG1IOVBmNmlXWm1OTld6Q1ZxekklMkZJb3hxOVZINk9Sa2dPbzlsbnFJbmZqd2MxSFE2N2tLZWQlMkJiJTJGbklHRkxFU3lZaSUyQmhyOFNkbGd6MkVoUnRmV3clMkJBN0t6Y0xTa3hrM2clM0QlM0Q; cto_bidid=yQDoLF9abDRGOGJ4JTJGNmpMQjVTcktHWkUxSmVyTUQ0THVxdmQlMkZLN01wcEFDbmMlMkZ4TVhFaGVTY1VBdmtNcTBhRHZCY3BnVXZwMnphbW4xJTJCWXNnZzZYcFhOQVhlVzFCbXRoOWdoR01qbVdTTXk3T2Y0JTNE; _ga_525WEYQTV9=GS1.1.1745551600.16.1.1745552045.60.0.0',
    'pragma':
    'no-cache',
    'priority':
    'u=2, i',
    'referer':
    'https://www.hltv.org/',
    'sec-ch-ua':
    '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'sec-fetch-dest':
    'image',
    'sec-fetch-mode':
    'no-cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'

}
params = {
    'auto': 'compress',
    'fm': 'avif',
    'ixlib': 'java-2.1.0',
    'm': '/m.png',
    'mw': '160',
    'mx': '30',
    'my': '710',
    'q': '75',
    'w': '1200',
    's': '81e3216bdbc532f15a905fec25931956'
}

res = requests.get(url=url, headers=my_headers, params=params)

print(res.content)  # 响应代码

# with open('test.html', 'wb') as f:
#     f.write(res.content)
with open('Practice.jpg', 'wb') as f:
    f.write(res.content)
