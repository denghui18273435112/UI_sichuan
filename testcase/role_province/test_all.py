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

    #@pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("Data",ExcelData("test_overview_digital"))
    def test_overview_digital(self,driver,Data):
        """数字概览：饼图统计"""
        self.assert_result = all(driver,Data).overview_digital()
    #@pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("Data",ExcelData("test_standard_direction"))
    def test_charts(self,driver,Data):
        """数字概览：参训/达标走势图"""
        self.assert_result = all(driver,Data).standard_direction()
    #@pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("Data",ExcelData("test_kinds_standards"))
    def test_kinds_standards(self,driver,Data):
        """数字概览：各类达标情况"""
        self.assert_result = all(driver,Data).kinds_standards()
    #@pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("Data",ExcelData("test_student_details"))
    def test_student_details(self,driver,Data):
        """学员详情：字段查询"""
        self.assert_result = all(driver,Data).student_details()
    #@pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("Data",ExcelData("test_company_data"))
    def test_company_data(self,driver,Data):
        """公司数据：查询导出"""
        self.assert_result = all(driver,Data).company_data()
    #@pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize("Data",ExcelData("test_PlanSubmit_01"))
    def test_PlanSubmit(self,driver,Data):
        """培训计划报送"""
        self.assert_result = all(driver,Data).PlanSubmit_01()
    #@pytest.mark.test
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("Data",ExcelData("test_query_inquire"))
    def test_query_inquire(self,driver,Data):
        """培训记录查询"""
        self.assert_result = all(driver,Data).query_inquire()
    #@pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=10)
    @pytest.mark.parametrize("Data",ExcelData("test_inquire_operation"))
    def test_inquire(self, driver,Data):
        """培训学分查询"""
        self.assert_result = all(driver,Data).inquire_operation()
    #@pytest.mark.test
    @pytest.mark.run(order=11)
    @pytest.mark.parametrize("Data",ExcelData("test_RecordImport_01"))
    def test_RecordImport(self,driver,Data):
        """培训记录导入"""
        self.assert_result = all(driver,Data).test_RecordImport()

    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_CreditInquire"))
    @pytest.mark.run(order=13)
    def test_CreditInquire(self,driver,Data):
        """培训记录统计-字段查询、按钮操作"""
        self.assert_result = all(driver,Data).test_CreditInquire()

    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_OnlineLearning"))
    @pytest.mark.run(order=14)
    def test_OnlineLearning(self,driver,Data):
        """ 在线学习-查看一下"""
        self.assert_result = all(driver,Data).test_OnlineLearning()

    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_TrainingExam_01"))
    @pytest.mark.run(order=15)
    def test_TrainingExam_01(self,driver,Data):
        """ 培训测评-培训测评 查询操作"""
        self.assert_result = all(driver,Data).test_TrainingExam_01()

    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_TrainingExam_02"))
    @pytest.mark.run(order=16)
    def test_TrainingExam_02(self,driver,Data):
        """ 培训测评-培训统计 查询操作"""
        self.assert_result = all(driver,Data).test_TrainingExam_02()

    @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_OD_inquire"))
    @pytest.mark.run(order=203)
    def test_OD_inquire(self,driver,Data):
        """ 输入的方式单个查询"""
        self.assert_result = all(driver,Data).OD_inquire()

    @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_Batch_query_Reset"))
    @pytest.mark.run(order=204)
    def test_Batch_query_Reset(self,driver,Data):
        """ 批量查询"""
        self.assert_result = all(driver,Data).Batch_query_Reset()

    @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_import_query"))
    @pytest.mark.run(order=205)
    def test_import_query(self,driver,Data):
        """导入查询"""
        self.assert_result = all(driver,Data).import_query()



