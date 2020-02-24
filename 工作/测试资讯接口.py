#Author:Timm

import requests, json
riqi = 20191209
pageNo = 32
pageSize = 50
reponse_str = requests.get(url="http://apigw.haier.net/news/getNewsByDate.do?ext_var=11393142619605&date={}"
                 "&pageNo={}&pageSize={}".format(riqi,pageNo,pageSize),headers=
                {"api_gateway_auth_app_id":"28e8e595-09c4-443e-9577-702d14094d9c",
                 "api_gateway_auth_app_password":"L3revdD4fdvx"}).json()
# print(reponse_str)
print(len(reponse_str["rows"]))