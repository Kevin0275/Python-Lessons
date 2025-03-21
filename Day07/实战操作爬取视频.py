import requests

url = 'https://kvideo01.youju.sohu.com/214763fa-10d2-4edb-9490-0b8a893436102_0_0.mp4?sign=97f4d5914841a36a270b694e6df5eeeb&t=1736195593'

response = requests.get(url)

# print(response.content)

with open('Test_video.mp4', 'wb') as f:
    f.write(response.content)