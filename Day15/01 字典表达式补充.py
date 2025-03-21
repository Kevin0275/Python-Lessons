# 目标：将 dic1 里面的所有字母大写并且组成一个新的字典

d1 = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3'
}

# 普通做法：
d2 = {}
for k, v in d1.items():
    d2[k.upper()] = v.upper()
print(d2)  # {'K1': 'V1', 'K2': 'V2', 'K3': 'V3'}

# 字典表达式
d3 = {key.upper(): val.upper() for key, val in d1.items()}
