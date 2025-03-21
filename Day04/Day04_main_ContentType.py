# Content Type格式，是浏览器和服务器之间联系的具体信息的一种规范，可能有的有，有的没有
a = 1
'''
Content Type一般用于明确请求体的格式，出现在请求头中，所以用于post请求

For example:

post 请求1：
“
post /login https/1.1
host: www.lagou.com
accept: text/plain/img/xml/*
User-agent: *
content_type:form

user=Kevin&password=<PASSWORD>  #使用=和&来拼接   url_encoded form表单格式
”

“
post 请求2:
post /login https/1.1
host: www.lagou.com
accept: text/plain/img/xml/*
User-agent: *
content_type:json

{'user': 'Kevin', 'password': '<PASSWORD>'} #json格式，类似字典
”


'''
