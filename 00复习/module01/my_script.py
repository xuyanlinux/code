import string
import random
pwd = ''.join(random.sample(string.digits + string.ascii_letters + '!@#$%^&*', 15))
print(pwd)