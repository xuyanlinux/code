#Author:Timmy
class ftp:
    def action(self):
        while True:
            s = input("cmd>>>").strip()
            if hasattr(self,s):
                cmd = getattr(self,s)
                cmd()
    def get(self):
        print("get....")
    def put(self):
        print("put....")


f = ftp()
setattr(f,'name',1212)
print(getattr(f,'name',None))
delattr(f,'name')
print(getattr(f,'name',None))