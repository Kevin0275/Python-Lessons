# 写模式：w是写字符串、wb是写字节

# f = open('声声慢.txt','w',encoding='utf-8')
# f.write('寻寻觅觅，冷冷清清，凄凄惨惨戚戚。\n')

# 要求：将声声慢每结尾的最后一个标点符号改成叹号

# 首先，读取文件
f_read = open('声声慢.txt','r',encoding='utf-8')

f_write_new = open('声声慢2.txt','w',encoding='utf-8')

# 提取每一行
for line in f_read:
    # print(line,end='')

    new_line = line.replace('。','!')
    f_write_new.write(new_line)

f_read.close()
f_write_new.close()


# 任务：将img拷贝一份
f_img = open('Test_img.jpg','rb')
f_new_img = open('Test_new_img.jpg','wb')
for line in f_img:
    f_new_img.write(line)
