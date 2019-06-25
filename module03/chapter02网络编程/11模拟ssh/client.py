#Author:Timmy
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8080))


while True:
    cmd = input('>>>>>>>').strip()
    if not cmd:continue  # 如果输入的是空字符，进入下一次循环
    phone.send(cmd.encode('gbk'))
    res = phone.recv(1024)
    print(res.decode('gbk'))

phone.close()