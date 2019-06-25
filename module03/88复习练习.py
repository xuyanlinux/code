import subprocess
res = subprocess.Popen('ipconfig',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
data = res.stdout.read()
print(len(data))
s = 'avc'
