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
    #身份证查询个人信息
    for x in ["431225199212061818","M30102575","362130197312312425","HO4983324"]:
        url1 = "http://sc.maintain.giiatop.com/api/member/DeleteMember"
        data1= {"idNumber":"{}".format(x)}
        header1 = {"Cookie":token}
        body1 = requests.post(url=url1,json=data1,headers=header1)
        body1.json()
        allure.attach(body=json.dumps(body1.json()), name="身份证查询个人信息查询返回的数据", attachment_type=allure.attachment_type.TEXT)

class Test_all(object):
    """四川分类系统"""

    @pytest.mark.test
    @pytest.mark.run(order=9999)
    def test_logion_succeed(self):
        """最后执行的用例，删除添加数据"""
        pass



