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


class Test_all(object):
    """四川分类系统"""

    def teardown_method(self):
        #所有的用例执行 截图、生成报告、判断
        self.assert_result[0].screenShots()
        alluer(self.assert_result[1])
        assert "通过" ==self.assert_result[1]["actual_result"]
    def setup_class(self):
        pass
    def teardown_class(self):
        pass
    def setup_method(self):
        pass

    @pytest.mark.account_login
    @pytest.mark.parametrize("Data",ExcelData("test_logion_fail"))
    @pytest.mark.run(order=103)
    def test_logion_fail(self,driver,Data):
        """账号登录：失败"""
        self.assert_result = all(driver,Data).test_logion_fail()


    @pytest.mark.account_login
    @pytest.mark.parametrize("Data",ExcelData("test_logion_succeed"))
    @pytest.mark.run(order=104)
    def test_logion_succeed(self,driver,Data):
        """账号登录：成功"""
        self.assert_result = all(driver,Data).test_logion_succeed()





