import requests

from Day07.实战操作爬取图片 import my_headers

url = 'https://v3-web.douyinvod.com/ce65da6070ee050ac7f3409ca7d585b3/677c1639/video/tos/cn/tos-cn-ve-15/oUbmIG9Z8DAc3gRpo9F1B7OQ1BeAkCweEnfq7E/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1811&bt=1811&cs=0&ds=4&ft=AJkeU_TERR0sD6C1SDg2Nc0iPMgzbLvtoB1U_4FXrSwSNv7TGW&mime_type=video_mp4&qs=0&rc=aDNlOTQ3N2Q6aTw0aGRoOEBpajdpZnQ5cml3dzMzNGkzM0AtNC9iYjE0NWAxYGEtYjZiYSNycS9qMmQ0Z3FgLS1kLTBzcw%3D%3D&btag=c0000e00028000&cquery=101r_100B_100H_100K_100o&dy_q=1736174522&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20250106224201DA7F669D5564F80A919B'

my_headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'referer':'https://v3-web.douyinvod.com/ce65da6070ee050ac7f3409ca7d585b3/677c1639/video/tos/cn/tos-cn-ve-15/oUbmIG9Z8DAc3gRpo9F1B7OQ1BeAkCweEnfq7E/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1811&bt=1811&cs=0&ds=4&ft=AJkeU_TERR0sD6C1SDg2Nc0iPMgzbLvtoB1U_4FXrSwSNv7TGW&mime_type=video_mp4&qs=0&rc=aDNlOTQ3N2Q6aTw0aGRoOEBpajdpZnQ5cml3dzMzNGkzM0AtNC9iYjE0NWAxYGEtYjZiYSNycS9qMmQ0Z3FgLS1kLTBzcw%3D%3D&btag=c0000e00028000&cquery=101r_100B_100H_100K_100o&dy_q=1736174522&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20250106224201DA7F669D5564F80A919B',
}

response = requests.get(url,headers=my_headers)

# print(response.content)

with open('QuQu.mp4', 'wb') as f:
    f.write(response.content)

