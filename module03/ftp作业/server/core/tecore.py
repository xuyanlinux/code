#Author:Timmy
import subprocess
cmd_obj = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout = cmd_obj.stdout.read()
stderr = cmd_obj.stderr.read()
print(stdout.decode(encoding = 'gbk'))