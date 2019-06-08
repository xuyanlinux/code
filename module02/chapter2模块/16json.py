# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/24

import json

# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# str_dic = json.dumps(dic)
# print(str_dic)
# print(type(str_dic))
#
# dic2 = json.loads(str_dic)
# print(dic2)
# print(type(dic2))

data = {'username':['李华','二愣子'],'sex':'male','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
# json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
print(json_dic2)