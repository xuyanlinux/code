#Author:Timmy
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # socket重复利用
phone.bind(('127.0.0.1',8080))

phone.listen(5)

print('starting...')

conn,client = phone.accept()
while True:
    try:  ## 客户端断开后，break，否则会异常退出，如果是linux系统，会有其他的解决办法
        data = conn.recv(1024)
        print("客户端的数据",data)
        conn.send(data.upper())
    except ConnectionResetError:
        print("客户端断开了连接。。。")
        break

conn.close()
phone.close()