# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/26

import subprocess

a = subprocess.run(['dir'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=False)