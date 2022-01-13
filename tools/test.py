import requests

#登录
data = {"type":"I","Name":"admin","Vcode":"denghui","Pwd":"c6c861c435a1e98caba3bf1cd594c48f"}
url = "http://sc.maintain.giiatop.com/base/home/Login"
header = {"Content-Type": "application/json"}
body = requests.post(url=url,json=data,headers=header)
token = "{0}={1}".format("sc.maintain.token",body.cookies["sc.maintain.token"])

#获取列表档案信息档案
url2 = "http://sc.maintain.giiatop.com/api/member/GetMemberTriningOffline"
data2= {"year":2022,"className":"","pageNum":1,"pageSize":20,"total":5,"createdTime":[]}
header2 = {"Cookie":token}
body2 = requests.post(url=url2,json=data2,headers=header2)
body2.json()

#获取需要删除的数据id
delete_id = 0
len_s= body2.json()["data"]["list"]
for x  in range(len(len_s)):
    if  len_s[x]["className"] == "测试数据1":
        delete_id = len_s[x]["id"]
        break

#删除档案数据
print(delete_id)
url3 = "http://sc.maintain.giiatop.com/api/home/TrainingClear"
data3= {"ids":[delete_id]}
header3 = {"Cookie":token}
body3 = requests.post(url=url3,json=data3,headers=header3)
print(body3.json())
