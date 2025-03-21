import requests
from lxml import etree

# 因为服务器会返回两种不同的数据：一种是json，一种是html，对于json，我们可以直接解json然后拿数据。
# 而对于html，因为是文本字符串，所以可以使用正则，但是由于html是有序的树状结构，也可以用xpath。

# 先拿一个百度的首页

url = 'https://www.baidu.com'
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

res = requests.get(url, headers=my_headers)

# print(res.text)

# 利用etree设定一个对象
ele = etree.HTML(res.text)
# print(ele)      # <Element html at 0x16e7a02dd00>
# print(type(ele))    # <class 'lxml.etree._Element'> 这是在lxml库里，etree包里的一个类

# 比如说我们需要一个热搜
# re_sou_1 = ele.xpath('/html/body/div[1]/div[1]/div[5]/div/div/div[3]/ul/li')

# print(re_sou_1)     # 返回的是一个列表，并且每个元素都是Element对象

# for i in re_sou_1:
    # 每一个元素都是Element，然后我们可以用xpath进行进一步的筛选
    # title = i.xpath('./a/span[2]/text()')[0]  # ./代表当前标签   /text()代表取用当前标签下的所有文本
    # print(title)

# 路径语法说明：
'''
（1）主路径
1. / 表示从根路径出发
2. // 表示从当前节点出发筛选所有的目标标签而不考虑相对位置，例如//a就是取所有的a标签
3. ./ 表示从当前节点出发再次进行xpath

（2）谓语
/li[2]  表示取我在这个当前节点下，第二个li标签
/li[last()]  表示取最后一个li标签
/li[last()-1]  表示取倒数第二个li标签
/li[position()<3]  表示取前两个li标签

//a[@title]  表示取所有带有title属性的a标签
//a[@title = 'xx']  表示取所有带有title属性而且title属性的值是xx的a标签
//a[@price>10]  作比较
//a[text() = 'xx']  该标签下需要带有xx文本

可以使用|来做或选择：//book/price|//book/title    连着price带着title
可以使用and来加强对于属性选择的限制 //book[@price="350" and title="you"]
可以使用@href获取属性值
'''

# 获取所有对应标题的链接：
# for i in re_sou_1:
#     link = i.xpath('./a/@href')[0]
    # print(link)


# 获取标题上一级：
# UpperEle = ele.xpath('//ul[@id="hotsearch-content-wrapper"]')[0]
# print(UpperEle)

#获取标题列表：
# title_list = UpperEle.xpath('.//span[@class="title-content-title"]/text()')
# print(title_list)

#获取链接列表
# link_list = UpperEle.xpath('.//a/@href')
# print(link_list)

#让他们一一对应：
# print(list(zip(title_list, link_list)))

# 模糊查询：/a[contains(href,'xx')] 只要这个标签下，有这个属性，并且这个属性里面带这几个字符，都可以

# 将element对象转换成一个str对象
'''
a = ele.xpath('//a[@href="xx"]')[0]     获取标签
result = etree.tostring(a, encoding='utf-8').decode('utf-8')    先编码再解码，编码用etree解码用python
'''

