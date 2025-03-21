import requests
from lxml import etree

cookies = {
    'll': '"118114"',
    'bid': 'wcl7lQUJ8tU',
    '_pk_id.100001.4cf6': 'c3c31914caf02585.1735888541.',
    '__utmz': '30149280.1735888541.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmz': '223695111.1735888541.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__yadk_uid': 'NwF9PaQHcfcZInDpD41Cs68aBQbOEIX6',
    '_vwo_uuid_v2': 'D9B05D9F1489F86833BA7D3F5D8E146F6|b2a8eebdac409c418f60f1ae16236ced',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1736652421%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D',
    '_pk_ses.100001.4cf6': '1',
    'ap_v': '0,6.0',
    '__utma': '30149280.1111302653.1735888541.1735888541.1736652421.2',
    '__utmb': '30149280.0.10.1736652421',
    '__utmc': '30149280',
    '__utma': '223695111.1642480806.1735888541.1735888541.1736652421.2',
    '__utmb': '223695111.0.10.1736652421',
    '__utmc': '223695111',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'll="118114"; bid=wcl7lQUJ8tU; _pk_id.100001.4cf6=c3c31914caf02585.1735888541.; __utmz=30149280.1735888541.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1735888541.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=NwF9PaQHcfcZInDpD41Cs68aBQbOEIX6; _vwo_uuid_v2=D9B05D9F1489F86833BA7D3F5D8E146F6|b2a8eebdac409c418f60f1ae16236ced; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1736652421%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1111302653.1735888541.1735888541.1736652421.2; __utmb=30149280.0.10.1736652421; __utmc=30149280; __utma=223695111.1642480806.1735888541.1735888541.1736652421.2; __utmb=223695111.0.10.1736652421; __utmc=223695111',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

response = requests.get('https://movie.douban.com/top250', cookies=cookies, headers=headers)

# print(response.text)

ele_root = etree.HTML(response.text)

movie_list = ele_root.xpath('//ol[@class="grid_view"]/li')
# print(len(Upperele))

movie_brief_info = []

for movie in movie_list:
    movie_link = movie.xpath('.//div[@class="hd"]/a/@href')[0]
    # print(movie_link)
    movie_title = movie.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
    # print(movie_title)
    movie_brief_info.append((movie_title, movie_link))
print(movie_brief_info)