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
    @pytest.mark.role_province
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize("Data",ExcelData("test_PlanSubmit_01"))
    def test_PlanSubmit(self,driver,Data):
        """培训计划报送"""
        self.assert_result = all(driver,Data).PlanSubmit_01()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=11)
    @pytest.mark.parametrize("Data",ExcelData("test_RecordImport_01"))
    def test_RecordImport(self,driver,Data):
        """培训记录导入"""
        self.assert_result = all(driver,Data).test_RecordImport()





