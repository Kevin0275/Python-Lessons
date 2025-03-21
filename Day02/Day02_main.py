# Python语句中如果不含 if, while 这类特殊语句，都是自上而下顺序执行并且每个语句只执行一次

# 语句和表达式：语句没有返回值，表达式有返回值

# a = 1 + 2 * 3
# 1+ 2 * 3 是表达式因为生成结果7，然而 a = 7是语句因为他是赋值操作，没有返回的值。

# 函数不一定，有的是语句有的是表达式。
# print(a)
# 这是语句，因为他返回值为 None，只是打印出来而已。
# type(a)
# 这是表达式，因为返回结果为 int 整型。

# 分支语句：使程序有选择的执行语句

# age = input("Enter your age: ")
# if int(age) >= 18:
#     print("You are old enough")
# else:
#     print("You are young")

# 循环语句，for and while

'''
while 条件：
    循环体
当条件为假，循环结束

for 循环当遍历完成，循环结束

强制结束：
break，结束当前循环
exit，退出整个程序
跳过某个条件：continue，跳过当前一步循环，开始下一个。

'''

# list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a']
# print(list1[::-1])
# print(list1[::2])

# 列表的一些内置方法。

# 1.元素的查找与修改
# 元素的修改是地址指向的改变 list1[0] = 1

# 2.元素的增加与删除：

# 元素的增加：append insert extend
# list1.append(1)  # 返回值为 None，作用是在列表的最后加入新的元素
# list1.insert(3, 1)  # 作用是将新的元素加入到index特定的位置

# list2 = [1, 2, 3, 1]
# list1.extend(list2)  # 作用是将一个列表里的所有元素按照原有顺序append到另外一个列表最后端。
# 虽然extend和列表加法都可以做到这件事情，但是extend是在原有基础上做的修改，而不是重新生成一个列表，效率要更高

# 元素的删除：pop remove clear
# list1.pop(-1)  # 按照索引删除对应元素，并且具有返回值，返回的是对应着该索引的元素，也就是被删的元素
# list2.remove(1)  # 删除与括号内元素相同的元素，也就是查找，删除，只不过删除的是找到的第一个元素

# 删除所有的相同元素、
# while 1 in list2:
#     list2.remove(1)
# print(list2)
#
# 3. 元素的出现次数计数
# list2.count(1)  # 计算元素 1 出现了多少次

# 4. 元素的排列（Attention：必须所有的元素都是数字才可以）
numbers_list = [1, 2, 4, 5.6, 21, -2]
numbers_list.sort()  # 在什么都不做要求的情况下，将所有元素升序排列
print(numbers_list)

'''
sort函数中包含两个关键字符：key 和 reverse，
key 是规定一个函数，abs，len，或者自定义的函数，然后将每一个列表中的元素输入到函数中，然后对于函数值
进行排列，之后让原列表中的原来的元素按照排列后的顺序进行重新排列
reverse 是最后的列表整理环节，这是一个bool值，默认为 False，如果是 True 的话，就会将列表按照 key
整理后的顺序进行排列，然后整个反向输出。
'''

# 元组，和列表高度相似，但是元组是不可变的，也就是只读。不过，由于其不能更改，一般用来存储一些重要数据
# 元组相对于更加灵活的列表所占据的内存空间要小得多，因为python不需要为它创建动态存储
'''
Attention: 对于python来说，(1) 这个元组被认为是数字1而不是只含有一个元素的元组，如果我们希望表示
           这是一个元组，那么可以写成：(1,)
'''

# 字典：字典由 Key 和对应的 Value 组成。相较于列表使用索引来管理元素，字典则更加复杂，不再使用0，1，2来管理
dic = {'name': 'John',
       'age': 18,
       'job': 'driver'
       }
# 字典使用 Key 来管理元素。

# dic['key'] = 'value'

# 增加一个：
dic['ExpectedValue'] = '$100'

# 修改：
dic['age'] = 20

# 是添加还是修改，取决于你的 Key 是不是已经存在于字典里面

# 删除一个：del
del dic  # 删除了字典
del dic['job']

'''
对于列表的循环，我们使用的是
for i in list
所有的i都是在列表里的所有元素

对于字典的循环，我们使用
for i in dic
所有的i都是字典里的 Key
'''

# 查看某个键的值：get
print(dic.get('job'))
# 我们当然可以使用 dic['job'] 来实现相同的功能，但是get要更加强大
# 这是因为如果我们想要查找的 Key 并不存在，get会返回 None 而不是报错。None是默认的值，如果我们想返回不同的值，
# 可以使用 dic.get('names','not founded')

# 增加和修改多个键的值：update
dic.update({'name': 'Smith', 'age': 27, 'country': 'US'})

# 删除
dic.pop('country')

# item语法
dic.keys()  # 得到的是一个列表，所有元素都是dict里面的key
dic.values()  # 得到的是一个列表，所有元素都是dict里面的value
dic.items()  # important：得到的是 [('name','Smith'), ('age', 27), ('country', 'US')]
# items 主要用于遍历字典

# 补充语法
x = 1  # 将1赋值给x

x, y = [1, 2]  # 将1，2分别赋值给x和y

x, *y = [1, 2, 3]  # 适用于前面变量的数量不等于后面的元素数量，加星号代表将后面所有的元素装在列表里赋值给y
# 如此，我们有 x = 1, y = [2, 3]

# 遍历字典
# 方法一：不推荐
for i in dic:
    print('Key=', i, 'Value=', dic[i])
# 方法二：
for k, v in dic.items():
    print('Key=', k, 'Value=', v)

# 这种方法是因为所有在 dic.items() 里面的元素都是一个二维元组，所以我们可以用固定的两个元素来承接。

# 函数：一种封装代码的手段

'''
函数结构：
def 函数名(形式变量):
    函数体
    
调用函数：
函数名(具体变量)

变量存在的意义是我们有的时候需要函数中有一些函数
'''

'''
def add(x, y):
    z = x + y
    return z


ret = add(1, 2)
print(ret)
'''
