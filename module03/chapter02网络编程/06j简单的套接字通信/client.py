#Author:Timmy
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8080))

phone.send('hello'.encode('utf-8'))
res = phone.recv(1024)
print(res)