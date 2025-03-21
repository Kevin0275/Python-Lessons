# 应用案例（1）

# 目的：拿到所有的百度网站首页上的热搜新闻标题

# (1) 爬虫：抓取百度网站首页
import requests

cookies = {
    'BAIDUID_BFESS': '22DF5F1F6DE9FC8F06EE7A88A243A433:FG=1',
    'newlogin': '1',
    'BIDUPSID': '22DF5F1F6DE9FC8F06EE7A88A243A433',
    'PSTM': '1735885257',
    'BD_UPN': '12314753',
    'ZFY': 'saa6NIUVZjzGTz8n:A7AlMnrBgreYRcHDNLWEwFgJHUY:C',
    'RT': '"z=1&dm=baidu.com&si=06a8b3e4-297e-4711-8cd4-6d3071c57705&ss=m5l54xin&sl=1&tt=799&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=817&ul=anf&hd=ani"',
    'H_PS_PSSID': '61027_60853_61530_61523_61608_61634_61680_61556_61694_61729_61733_61738_61782_61790_61805',
    'BD_HOME': '1',
    'BA_HECTOR': '8g2g2084a42g25agahaga0a0bb2ijm1jo4edc1u',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'BAIDUID_BFESS=22DF5F1F6DE9FC8F06EE7A88A243A433:FG=1; newlogin=1; BIDUPSID=22DF5F1F6DE9FC8F06EE7A88A243A433; PSTM=1735885257; BD_UPN=12314753; ZFY=saa6NIUVZjzGTz8n:A7AlMnrBgreYRcHDNLWEwFgJHUY:C; RT="z=1&dm=baidu.com&si=06a8b3e4-297e-4711-8cd4-6d3071c57705&ss=m5l54xin&sl=1&tt=799&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=817&ul=anf&hd=ani"; H_PS_PSSID=61027_60853_61530_61523_61608_61634_61680_61556_61694_61729_61733_61738_61782_61790_61805; BD_HOME=1; BA_HECTOR=8g2g2084a42g25agahaga0a0bb2ijm1jo4edc1u',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.baidu.com/', cookies=cookies, headers=headers)

# print(response.text)

# (2) 数据解析
import re

# 通过浏览器的分析，我们发现所有的热搜标题都符合：<span class="title-content-title">*</span>
# 所以我们就可以抓取中间的字符：

res = re.findall('<span class="title-content-title">.*?</span>', response.text, re.S)

for i in res:
    i = i.replace('<span class="title-content-title">','')
    i = i.replace('</span>','')
    print(i)
print(len(res))