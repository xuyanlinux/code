#Author:Timmy
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(('127.0.0.1',8080))

phone.listen(5)

print('starting...')

conn,client = phone.accept()

data = conn.recv(1024)
conn.send(data.upper())

conn.close()