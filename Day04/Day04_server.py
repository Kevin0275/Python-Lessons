import socket

server = socket.socket()
server.bind(('127.0.0.1',8000))
server.listen(5)

while True:
    client,address = server.accept()

    data = client.recv(1024)
    print(data.decode())

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Wish you a good day!</h1>"
    client.send(response.encode())
    client.close()