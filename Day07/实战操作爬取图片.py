import requests

url = 'http://pic.netbian.com/uploads/allimg/241028/001351-1730045631c412.jpg'
# print(type(requests.get(url).content))
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'Cookie': 'cf_clearance=jAsHjm2RIk.tO909uL6y17aNkdVpOmO2ZtKxuY3yNG8-1736172731-1.2.1.1-foPER5joKN4RynQfgSCGj6b4vqK.zU8YQa9jiYoCBgO4jjyfyETERAOJP8JLRd6ZCu4TIL2K1PKsuo25uyCsbZ3xp3_uv5FKJ7YHJGyme7vQR9rUQS95qlHx1t__C_5w9WeQaBypdXE_KQaPI7L3Zcz0K8DbnV2Y8DwLjpuMK0Ou2AtK.8NCuNKc5pBlP9jXCVLkcI43w1JFDpN1pbTK_DKqmL94M.qJrFxPj6Jhx__09dL_g_kRQ4plzHAhbs8wxIJkj_z6gqnqScWHUF4yTRiFSYGs3sLYq6Qn2NWnEu.IdxmtP9V9t5ubZh2HnUxCkVkwHp09HN3v9XxvhVdWEDyNAvA_Tfw62OrFnEFHf61cGI9fkik9qOWBrg62MMngf9lWL5JneTVTRw3bcvN1nMAxrRBpv2wAcGVK0JwGBLjIfGW35M6Bid1vAJf544yf; zkhanecookieclassrecord=%2C54%2C'
}
res = requests.get(url=url, headers=my_headers)

print(res.content)

# with open('test.html', 'wb') as f:
#     f.write(res.content)
with open('Practice.jpg', 'wb') as f:
    f.write(res.content)
