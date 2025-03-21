import json

# json.dumps()    #序列化：将Python的结构化数据转换为json格式的字符串
# json.loads()    #反序列化：将json格式的字符串转换为本语言的结构化数据

data = {
    'Name': 'Kevin',
    'Age': 18,
    'Status': "A1",
    'Married': False,
    'Gender': 'Male',
    'GirlFriend': None
}

data = json.dumps(data)
print(data)     #Attention: json字符串虽然和字典很像，但是完全不一样

# 返回：{"Name": "Kevin", "Age": 18, "Status": "A1", "Married": false, "Gender": "Male", "GirlFriend": null}

'''
JS(JavaScript):

JSON.stringify()    #序列化
JSON.parse()    #反序列化
'''
