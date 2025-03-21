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
