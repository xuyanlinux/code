#Author:Timmy
import socket
import configparser
from conf import setting
class server():
    def __init__(self):
        self.userinfo = self.load_user_info()
    def load_user_info(self):
        file_path = setting.USERDB_FILE
        user_info = configparser.ConfigParser()
        user_info.read(file_path)
        return user_info
    def login(self,username,password):
        """验证用户"""
        pass
    def login(self):
        pass
    def run(self):
        count = 0
        while  True:
            print(count)
            count += 1
            if count == 10:
                break
