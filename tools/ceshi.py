import json

import requests
data = {"type":"I","Name":"admin","Vcode":"denghui","Pwd":"c6c861c435a1e98caba3bf1cd594c48f"}
url = "http://sc.maintain.giiatop.com/base/home/Login"
header = {"Content-Type": "application/json"}
body = requests.post(url=url,json=data,headers=header)
token = "{0}={1}".format("sc.maintain.token",body.cookies["sc.maintain.token"])
print(token)

url1 = "http://sc.maintain.giiatop.com/api/member/Infos"
data1= {"idNumber":"431225199212061818"}
header1 = {"Cookie":token}
body1 = requests.post(url=url1,json=data1,headers=header1)
print(type(json.dumps(body1.json())))