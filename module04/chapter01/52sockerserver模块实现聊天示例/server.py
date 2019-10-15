#Author:Timmy
import socketserver
'''
使用sockerserver模块的套路，三大步：
First, you must create a request handler class by subclassing the BaseRequestHandlerclass and overriding its handle() method; 
this method will process incoming requests. 　
　
Second, you must instantiate one of the server classes, passing it the server’s address and the request handler class.

Then call the handle_request() or serve_forever() method of the server object to process one or many requests.
Finally, call server_close() to close the socket.
'''
class MyServer(socketserver.BaseRequestHandler):
        def handle(self):
            while True:
                try:
                    client_data = self.request.recv(1024)
                    if len(client_data) == 0:
                        print("客户端断开连接，等待新的用户连接...")
                        break
                    print("接受数据>>>",str(client_data,'utf-8'))
                    response = input("响应数据>>>").strip()
                    self.request.sendall(bytes(response,'utf-8'))
                except ConnectionResetError:
                    break
            self.request.close()


server = socketserver.ThreadingTCPServer(('127.0.0.1',88),MyServer)
server.serve_forever()