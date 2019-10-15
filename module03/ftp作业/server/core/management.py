#Author:Timmy
from core import main


class ManagementTool:
    def __init__(self,args):
        self.arg = args

    def execute(self):
        if len(self.arg) != 2:
            self.usage()
        else:
            cmd = self.arg[1]
            if not hasattr(self,cmd):
                print("invalid argument!")
                self.usage()
            else:
                act = getattr(self,self.arg[1])
                act()

    def start(self):
        print("server start".center(50,'*'))
        server = main.server()
        server.run()
    def usage(self):
        print("USAGE: "
              "server start|creatuser")
