from hashlib import md5

md5_obj = md5()

with open('02data.log') as f:
    for line in f:
        md5_obj.update(line.encode('utf-8'))

print(md5_obj.hexdigest())