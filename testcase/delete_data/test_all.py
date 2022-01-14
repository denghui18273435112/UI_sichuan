import pytest
from tools.Yaml_read import Yaml_read
from lib.all import *
from tools.ExcelData import *
import pytest
from tools.Yaml_read import Yaml_read
from lib.all import *
from tools.ExcelData import *
import pytest
from tools.Yaml_read import Yaml_read
from lib.all import *
from tools.ExcelData import *
import time
import win32gui
import traceback
import allure
import win32con
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tools.Base import *
from tools.WinUpLoadFile import upload_files
from tools.Yaml_read import Yaml_read
import requests

def setup_module():
    allure.attach(body="TEST-01", name="所有用例执行前，执行一次", attachment_type=allure.attachment_type.TEXT)
def teardown_module():
    allure.attach(body="TEST-06", name="所有用例执行完，执行一次", attachment_type=allure.attachment_type.TEXT)
    #登录
    data = {"type":"I","Name":"admin","Vcode":"denghui","Pwd":"c6c861c435a1e98caba3bf1cd594c48f"}
    url = "http://sc.maintain.giiatop.com/base/home/Login"
    header = {"Content-Type": "application/json"}
    body = requests.post(url=url,json=data,headers=header)
    token = "{0}={1}".format("sc.maintain.token",body.cookies["sc.maintain.token"])
    allure.attach(body=token, name="登录后拼接的token", attachment_type=allure.attachment_type.TEXT)

    #身份证查询个人信息 删除
    for x in ["431225199212061818","M30102575","362130197312312425","HO4983324"]:
        url1 = "http://sc.maintain.giiatop.com/api/member/DeleteMember"
        data1= {"idNumber":"{}".format(x)}
        header1 = {"Cookie":token}
        body1 = requests.post(url=url1,json=data1,headers=header1)
        body1.json()
        allure.attach(body=json.dumps(body1.json()), name="身份证查询个人信息查询返回的数据", attachment_type=allure.attachment_type.TEXT)

    #获取列表档案信息档案
    url2 = "http://sc.maintain.giiatop.com/api/member/GetMemberTriningOffline"
    data2= {"year":2022,"className":"","pageNum":1,"pageSize":20,"total":5,"createdTime":[]}
    header2 = {"Cookie":token}
    body2 = requests.post(url=url2,json=data2,headers=header2)
    body2.json()
    allure.attach(body=json.dumps(body2.json()), name="获取档案的列表数据", attachment_type=allure.attachment_type.TEXT)

    #获取需要删除的数据id
    delete_id = []
    len_s= body2.json()["data"]["list"]
    for x  in range(len(len_s)):
        if  len_s[x]["className"] == "测试数据20138":
            delete_id.append(len_s[x]["id"])

    #删除档案数据
    for x  in delete_id:
        url3 = "http://sc.maintain.giiatop.com/api/home/TrainingClear"
        data3= {"ids":[x]}
        header3 = {"Cookie":token}
        body3 = requests.post(url=url3,json=data3,headers=header3)
        body3.json()
        allure.attach(body=json.dumps(body3.json()), name="删除档案数据", attachment_type=allure.attachment_type.TEXT)


class Test_all(object):
    """四川分类系统"""
    def setup_class(self):
        allure.attach(body="TEST-02", name="每个类开始执行一次", attachment_type=allure.attachment_type.TEXT)
    def setup_method(self):
        allure.attach(body="TEST-03", name="每个方法开始执行", attachment_type=allure.attachment_type.TEXT)
    def teardown_method(self):
        #所有的用例执行 截图、生成报告、判断
        allure.attach(body="TEST-04", name="每个方法结束执行", attachment_type=allure.attachment_type.TEXT)
        self.assert_result[0].screenShots()
        alluer(self.assert_result[1])
        assert "通过" ==self.assert_result[1]["actual_result"]
    def teardown_class(self):
        allure.attach(body="TEST-05", name="每个类结束执行一次", attachment_type=allure.attachment_type.TEXT)

    # @pytest.mark.test
    @pytest.mark.delete_data
    @pytest.mark.parametrize("Data",ExcelData("test_delete_data"))
    @pytest.mark.run(order=9999)
    def test_delete_data(self,driver,Data):
        """最后执行的用例，删除添加数据"""
        self.assert_result = all(driver,Data).test_delete_data()



