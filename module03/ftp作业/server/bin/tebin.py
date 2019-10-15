#Author:Timmy

import os,sys
import hashlib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)

from core import tecore

tecore.print_core()

hash = hashlib.md5()
hash.update(b'123456')
print(hash.hexdigest())

h = hashlib.md5(b'123456')
print(h.hexdigest())