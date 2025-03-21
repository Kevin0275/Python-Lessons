# 网址：https://game.51.com/search/action/game

import requests

url = 'https://game.51.com/search/action/game'

game = input('请输入游戏名：')

my_params = {
    'q': game
}

res = requests.get(url, params=my_params)

res.encoding = 'utf-8'

res_text = res.text

print(res_text)

# with open('51游戏.html', 'wb') as f:
#     f.write(res.content)

with open('51游戏w.html', 'w', encoding='utf8') as f:
    f.write(res_text)
# print(res.text)
