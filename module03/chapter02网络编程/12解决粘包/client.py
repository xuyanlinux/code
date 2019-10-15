#Author:Timmy
import socket
import struct
import json

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8080))


while True:
    cmd = input('>>>>>>>').strip()
    if cmd.upper() == 'Q':
        break
    if not cmd:continue  # 如果输入的是空字符，进入下一次循环
    phone.send(cmd.encode('gbk'))

    head_struct = phone.recv(4)
    head_json_len = struct.unpack('i',head_struct)[0]
    head_json_bytes = phone.recv(head_json_len)
    head_json = head_json_bytes.decode('utf-8')
    head = json.loads(head_json)

    data_len = head['data_size']
    print(data_len)


    #开始收数据
    recv_size = 0
    recv_data = b''
    while recv_size < data_len:
        recv_data += phone.recv(1024)
        recv_size += len(recv_data)
        # recv_size = len(recv_data)
    print(recv_size)
    print(recv_data.decode('gbk'))
phone.close()