#Author:Timmy

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST =  "0.0.0.0"
PORT = 9999

USER_HOME_DIR = os.path.join(BASE_DIR,'home')

USERDB_FILE = "%s/conf/userdb.info" % BASE_DIR

MAX_SOCKET_LISTEN = 5