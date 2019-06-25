#Author:Timmy
import socket
import subprocess
import struct
import json
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # socket重复利用
phone.bind(('127.0.0.1',8080))

phone.listen(5)

print('starting...')
while True:  # 连接链接循环，解决每次客户端断开服务端就退出的问题
    conn,client = phone.accept()
    while True:
        try:  ## 客户端断开后，break，否则会异常退出，如果是linux系统，会有其他的解决办法
            cmd = conn.recv(1024).decode('gbk')
            print("客户端的数据",cmd)
            res = subprocess.Popen(cmd,
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            data = res.stdout.read()+res.stderr.read()

            data_size = len(data)
            headers = {'data_size':data_size}
            header_json = json.dumps(headers)
            header_json_bytes = bytes(header_json,encoding='gbk')
            conn.send(struct.pack('i',len(header_json_bytes)))

            conn.send(header_json_bytes)
            conn.send(data)
        except ConnectionResetError:
            print("客户端断开了连接。。。")
            break
        except ConnectionAbortedError:
            print("客户终止开了连接。。。")
            break

    conn.close()
phone.close()