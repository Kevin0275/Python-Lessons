import os
import time
import re
import requests
from lxml import etree

# 四大名著集合的url
set_url = 'https://5000yan.com/fenlei/sidamingzhu/'

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}


def outputHTML(url):
    res = requests.get(url, headers=my_headers)
    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    return html

def reRelease(string):
    # 正则匹配，拿到所有的无关符号：
    # 去掉 ，由一个\xa0引起
    string = re.sub(r'\xa0', '', string)

    # 去掉由它引起的多余换行
    string = re.sub(r'(\r\n\t){2}', r'\r\n\t', string)

    return string

set_html = outputHTML(set_url)

book_ele = set_html.xpath('//div[@class="list-group-flush "]/a')
# print(len(book_ele))

# 遍历四大书籍：
for book_info in book_ele:
    book_title = book_info.xpath('./div/h5/text()')[0]
    # print(book_title)
    print(f'开始下载{book_title}')

    # 创建文件夹：
    os.makedirs(f'作业/{book_title}', exist_ok=True)

    book_url = book_info.xpath('./@href')[0]

    # 访问书籍具体url
    book_html = outputHTML(book_url)

    chapter_info = book_html.xpath('//li[@class="p-2"]/a')
    # print(len(chapter_info))

    # 创建一个章节计数器
    chapter_num = 1

    # 遍历章节：
    for chapter_info in chapter_info:

        chapter_title = chapter_info.xpath('./text()')[0]

        chapter_title = re.sub(r'[*|?/><:"\\]', '', chapter_title)

        chapter_url = chapter_info.xpath('./@href')[0]

        # 去拿chapter的数据：（每次空两秒）
        time.sleep(2)
        chapter_content_html = outputHTML(chapter_url)

        chapter_content = chapter_content_html.xpath('//div[@class="grap"]/div')

        # 创建空字符串放文档
        content_str = ''
        for content_ele in chapter_content:
            content = content_ele.xpath('./text()')[0]
            content_str = content_str + content

        content_str = reRelease(content_str)
        content_str = content_str.strip()
        content_str = '\t' + content_str

        book_title = book_title.strip()

        with open(f'作业/{book_title}/{chapter_num}.{chapter_title}.txt', 'w', encoding='utf-8') as f:
            f.write(content_str)

        chapter_num = chapter_num + 1
        print(f'{chapter_title}', '下载完成！')



