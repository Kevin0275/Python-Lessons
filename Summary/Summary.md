# Basic of Python

### 一些值

1. string字符串

   1. 反斜杠 \ ， 取消转义

   2. 格式化：两种方法

      1. ```python
         f'This is the {example}.'
         ```

      2. ```python
         'This is the %s.' % (example)
         ```

   3. 内置方法：

      1. ```python
         s.upper()
         s.lower()
         s.startswith()
         s.endswith()
         s.split(' ')
         s.strip()
         ''.join(list)
         s.find()	-1
         s.index()	ValueError
         s.replace('',' ')
         ```

2. list列表

   1. 内置方法：
      ```py
      s1 = list[1]
      list.append(s2)
      list.insert(s2)
      list.extend(l2)
      list.pop(-1)	index
      list.remove(2)	element
      list.count(1)	element
      list.sort(key=,reverse=)	
      ```

3. 元组

   list，more simple

4. dic字典

   1. 内置方法
      ```python
      dic['key'] = 'value'
      del dic
      del dic['key']
      dic.update({'key1':'value1','key2':'value2'})
      dic.pop('')
      dic.get('')
      dic.keys()
      dic.values()
      dic.items()
      ```

5. class类

   1. 主要结构
      ```python
      class HKU:
          def __init__(self,name):
              self.name = name
          def getname(name):
              print(self.name)
      ```

   2. 一些方法

      ```python
      class student:
          def __init__(self, name,age):
              self.name = name
              self.age = age
          
          @classmethod
          def from_string(cls,data):
              name, age = data.split(',')
              return cls(name, int(age))
          
          @staticmethod
          def add(a,b):
              return a+b
          
      k = student.from_string('kevin-20')
      print(k.name)
      print(k.age)
      
      print(student.add(2,3))
      ```

6. bool
   1. True or False
   2. 一些特定的元素表示False，并且对于每一个数据类型，有且只有一个False

### 循环

1. for
2. while
3. （continue，break，exit）

### 判断

​	if

# HTTP and Web

1. HTTP是协议规范，请求/响应模式，无状态保存
2. server和client是基于包的传输，HTTP是对于这个包的规范
3. URL: 'https://www.baidu.com/s?wd=python'
   1. 首先，https，协议的名字
   2. IP地址，不过这里用的是www.baidu.com是域名
   3. 端口：默认80
   4. 路径：/s
   5. 查询参数：wd=python
4. 浏览器组装的请求：
   1. 请求首行
   2. 请求头
   3. 请求体

5. 两种不同的请求方式：get and post

6. ```python
   import socket
   
   server = socket.socket()  # 创建一个socket对象
   server.bind(('127.0.1.1', 8120))  # 提供运行的ip地址和端口
   server.listen(5)  # 监听数量
   
   conn, addr = server.accept()  # Conn是客户端在访问我们的服务器的时候传输过来的，客户端自己的socket
   # 程序在这里会阻塞住，等待客户端的访问
   
   # conn.recv() #接收数据
   # conn.send() #发送数据
   
   data = conn.recv(1024)  # 接收数据，接收数据最大数据为 1K
   
   print(data.decode())  # 因为data是字节，我们需要将它转译成字符串
   
   ret = 'Hello, master!'
   
   # conn.send(ret.encode()) #encode是将字符串转换成字节模式
   
   # 然而，我们依然在浏览器中接收不到 ret 的字符，这是因为我们的服务器发送了不按照HTTP协议的数据，导致了我们的
   # 浏览器无法阅读响应
   
   # 为满足HTTP协议：
   ret1 = 'HTTP/1.1 200 ok /r/n/r/nHello, master!'
   conn.send(ret1.encode())
   
   ```

7. 