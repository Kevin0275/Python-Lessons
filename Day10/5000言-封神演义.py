import requests
from lxml import etree
import os
import time
import re

book_url = 'https://fengshen.5000yan.com/'

my_headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

# 封神的目录页
response = requests.get(book_url, headers=my_headers)

response.encoding = 'utf-8'

os.makedirs('封神演义', exist_ok=True)

# print(response.text)

catalogue_page = etree.HTML(response.text)

# 所有的章节title和url
chapter_info_list = catalogue_page.xpath('//li[@class="p-2"]')
# print(len(chapter_info_list)) # 100章

for chapter_info in chapter_info_list:
    # 拿到每一章的标题：
    chapter_title = chapter_info.xpath('./a/text()')[0]
    # print(chapter_title)

    # 拿到每一章的链接：
    chapter_url = chapter_info.xpath('./a/@href')[0]
    # print(chapter_url)

    # 针对于每一章的链接发起请求：（每次请求间隔2s）
    time.sleep(2)
    chapter_res = requests.get(chapter_url, headers=my_headers)

    chapter_res.encoding = 'utf-8'

    chapter_html = etree.HTML(chapter_res.text)

    chapter_content = chapter_html.xpath('//div[@class="grap"]/div')
    # print(chapter_content)

    content_str = ''    # 空字符以存放文本

    for chapter_content in chapter_content:
        content = chapter_content.xpath('./text()')[0]
        content_str += content

    # print(repr(content_str))

    # 正则匹配，拿到所有的无关符号：
    # 去掉 ，由一个\xa0引起
    content_str = re.sub(r'\xa0', '', content_str)
    # print(repr(content_str))

    # 去掉由它引起的多余换行
    content_str = re.sub(r'(\r\n\t){2}', r'\r\n\t', content_str)
    # print(repr(content_str))

    with open(f'封神演义/{chapter_title}.txt', 'w', encoding='utf-8') as f:
        f.write(content_str)

    print(chapter_title, '下载完成！')


