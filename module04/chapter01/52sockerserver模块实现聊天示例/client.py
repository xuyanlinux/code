#Author:Timmy

import socket

ip_port = ('127.0.0.1',88)
sock = socket.socket()
sock.connect(ip_port)

print("客户端启动：")

while True:
    try:
        inp = input("发送数据>>>").strip()
        if inp == "exit":
            break
        sock.sendall(bytes(inp,'utf-8'))
        server_response = sock.recv(1024)
        print("服务端响应数据：",str(server_response,'utf-8'))
    except ConnectionResetError:
        print("快去看看，server端掉线了...")
        break