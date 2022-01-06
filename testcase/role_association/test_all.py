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
    @pytest.mark.role_association
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("Data",ExcelData("test_tabulate_data"))
    def test_tabulate_data(self,driver,Data):
        """汇总数据：查询"""
        self.assert_result = all(driver,Data).tabulate_data()

    @pytest.mark.role_association
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize("Data",ExcelData("test_PlanSubmit_02"))
    def test_PlanSubmit(self,driver,Data):
        """培训计划报送：操作退回"""
        self.assert_result = all(driver,Data).PlanSubmit_02()

    @pytest.mark.role_association
    @pytest.mark.run(order=12)
    @pytest.mark.parametrize("Data",ExcelData("test_TrainingFileManage"))
    def test_TrainingFileManage(self,driver,Data):
        """ 培训档案管理"""
        self.assert_result = all(driver,Data).test_TrainingFileManage()

    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_account_management_inquire"))
    @pytest.mark.run(order=101)
    def test_account_management_inquire(self,driver,Data):
        """账号管理-查询/按钮操作"""
        self.assert_result = all(driver, Data).account_management_inquire()

    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_account_management_add"))
    @pytest.mark.run(order=102)
    def test_account_management_add(self,driver,Data):
        """账号管理-账号添加"""
        self.assert_result = all(driver, Data).test_account_management_add()

    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_account_management_delete"))
    @pytest.mark.run(order=105)
    def test_account_management_delete(self,driver,Data):
        """账号管理-账号删除"""
        self.assert_result = all(driver,Data).test_account_management_delete()

    @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_IncumbentImport"))
    @pytest.mark.run(order=201)
    def test_IncumbentImport(self,driver,Data):
        """在职人员管理-导入页面：导入操作"""
        self.assert_result = all(driver,Data).test_IncumbentImport()

    @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_LeaversImport"))
    @pytest.mark.run(order=202)
    def test_LeaversImport(self,driver,Data):
        """离职人员管理-导入页面：导入操作"""
        self.assert_result = all(driver,Data).test_LeaversImport()

    @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_update_01"))
    @pytest.mark.run(order=206)
    def test_update_01(self,driver,Data):
        """个人信息修改"""
        self.assert_result = all(driver,Data).test_update_01()