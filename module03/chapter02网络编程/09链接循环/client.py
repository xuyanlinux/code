#Author:Timmy
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8080))


while True:
    mes = input('>>>>>>>').strip()
    if not mes:continue  # 如果输入的是空字符，进入下一次循环
    phone.send(mes.encode('utf-8'))
    res = phone.recv(1024)
    print(res)

phone.close()