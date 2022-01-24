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

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("Data",ExcelData("test_standard_direction"))
    def test_charts(self,driver,Data):
        """数字概览：参训/达标走势图"""
        self.assert_result = all(driver,Data).standard_direction()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("Data",ExcelData("test_kinds_standards"))
    def test_kinds_standards(self,driver,Data):
        """数字概览：各类达标情况"""
        self.assert_result = all(driver,Data).kinds_standards()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("Data",ExcelData("test_student_details"))
    def test_student_details(self,driver,Data):
        """学员详情：字段查询"""
        self.assert_result = all(driver,Data).student_details()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("Data",ExcelData("test_company_data"))
    def test_company_data(self,driver,Data):
        """公司数据：查询导出"""
        self.assert_result = all(driver,Data).company_data()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("Data",ExcelData("test_tabulate_data"))
    def test_tabulate_data(self,driver,Data):
        """汇总数据：查询"""
        self.assert_result = all(driver,Data).tabulate_data()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize("Data",ExcelData("test_PlanSubmit_02"))
    def test_PlanSubmit(self,driver,Data):
        """培训计划报送：操作退回"""
        self.assert_result = all(driver,Data).PlanSubmit_02()

     # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("Data",ExcelData("test_query_inquire"))
    def test_query_inquire(self,driver,Data):
        """培训记录查询"""
        self.assert_result = all(driver,Data).query_inquire()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.run(order=10)
    @pytest.mark.parametrize("Data",ExcelData("test_inquire_operation"))
    def test_inquire(self, driver,Data):
        """培训学分查询"""
        self.assert_result = all(driver,Data).inquire_operation()

    # @pytest.mark.test
    @pytest.mark.run(order=12)
    @pytest.mark.parametrize("Data",ExcelData("test_TrainingFileManage"))
    def test_TrainingFileManage(self,driver,Data):
        """ 培训档案管理：审核导入数据"""
        self.assert_result = all(driver,Data).test_TrainingFileManage()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_CreditInquire"))
    @pytest.mark.run(order=13)
    def test_CreditInquire(self,driver,Data):
        """培训记录统计-字段查询、按钮操作"""
        self.assert_result = all(driver,Data).test_CreditInquire()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_OnlineLearning"))
    @pytest.mark.run(order=14)
    def test_OnlineLearning(self,driver,Data):
        """ 在线学习-查看一下"""
        self.assert_result = all(driver,Data).test_OnlineLearning()

    # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_TrainingExam_01"))
    @pytest.mark.run(order=15)
    def test_TrainingExam_01(self,driver,Data):
        """ 培训测评-培训测评 查询操作"""
        self.assert_result = all(driver,Data).test_TrainingExam_01()

     # @pytest.mark.test
    @pytest.mark.role_province
    @pytest.mark.parametrize("Data",ExcelData("test_TrainingExam_02"))
    @pytest.mark.run(order=16)
    def test_TrainingExam_02(self,driver,Data):
        """ 培训测评-培训统计 查询操作"""
        self.assert_result = all(driver,Data).test_TrainingExam_02()

########################################################################################
########################################################################################
########################################################################################

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_account_management_inquire"))
    @pytest.mark.run(order=101)
    def test_account_management_inquire(self,driver,Data):
        """账号管理-查询/按钮操作"""
        self.assert_result = all(driver, Data).account_management_inquire()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_account_management_add"))
    @pytest.mark.run(order=102)
    def test_account_management_add(self,driver,Data):
        """账号管理-账号添加"""
        self.assert_result = all(driver, Data).test_account_management_add()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_account_management_delete"))
    @pytest.mark.run(order=105)
    def test_account_management_delete(self,driver,Data):
        """账号管理-账号删除"""
        self.assert_result = all(driver,Data).test_account_management_delete()

########################################################################################
########################################################################################
########################################################################################

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_IncumbentImport"))
    @pytest.mark.run(order=201)
    def test_IncumbentImport(self,driver,Data):
        """在职人员管理-导入页面：导入操作"""
        self.assert_result = all(driver,Data).test_IncumbentImport()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_LeaversImport"))
    @pytest.mark.run(order=202)
    def test_LeaversImport(self,driver,Data):
        """离职人员管理-导入页面：导入操作"""
        self.assert_result = all(driver,Data).test_LeaversImport()

    #@pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_OD_inquire"))
    @pytest.mark.run(order=203)
    def test_OD_inquire(self,driver,Data):
        """ 输入的方式单个查询"""
        self.assert_result = all(driver,Data).OD_inquire()

    #@pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_Batch_query_Reset"))
    @pytest.mark.run(order=204)
    def test_Batch_query_Reset(self,driver,Data):
        """ 批量查询"""
        self.assert_result = all(driver,Data).Batch_query_Reset()

    #@pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_import_query"))
    @pytest.mark.run(order=205)
    def test_import_query(self,driver,Data):
        """导入查询"""
        self.assert_result = all(driver,Data).import_query()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_update_01"))
    @pytest.mark.run(order=206)
    def test_update_01(self,driver,Data):
        """个人信息修改"""
        self.assert_result = all(driver,Data).test_update_01()

    @pytest.mark.skip
    @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_IncumbentManage"))
    @pytest.mark.run(order=207)
    def test_IncumbentManage(self,driver,Data):
        """在职人员管理"""
        self.assert_result = all(driver,Data).test_IncumbentManage()

        # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_LeaversManage"))
    @pytest.mark.run(order=208)
    def test_LeaversManage(self,driver,Data):
        """离职人员管理"""
        self.assert_result = all(driver,Data).test_LeaversManage()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_EntryPersonInquiry_01"))
    @pytest.mark.run(order=209)
    def test_EntryPersonInquiry(self,driver,Data):
        """入职人员查询"""
        self.assert_result = all(driver,Data).test_EntryPersonInquiry()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_OnJobPersonInquiry"))
    @pytest.mark.run(order=210)
    def test_OnJobPersonInquiry(self,driver,Data):
        """在职人员查询"""
        self.assert_result = all(driver,Data).test_OnJobPersonInquiry()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_ResignPersonInquiry"))
    @pytest.mark.run(order=211)
    def test_ResignPersonInquiry(self,driver,Data):
        """离职人员查询"""
        self.assert_result = all(driver,Data).test_ResignPersonInquiry()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_ProfessionRecordSend_01"))
    @pytest.mark.run(order=212)
    def test_ProfessionRecordSend(self,driver,Data):
        """执业备案报送"""
        self.assert_result = all(driver,Data).test_ProfessionRecordSend_01()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_ProfessionRecordSend_02"))
    @pytest.mark.run(order=213)
    def test_ProfessionRecordSend(self,driver,Data):
        """执业备案报送：协会查看、删除"""
        self.assert_result = all(driver,Data).test_ProfessionRecordSend_02()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_LicenseImportTrack_02"))
    @pytest.mark.run(order=214)
    def test_LicenseImportTrack(self,driver,Data):
        """执业证导入追踪：所有的操作"""
        self.assert_result = all(driver,Data).test_LicenseImportTrack_02()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_ProfessionRecordStatistics"))
    @pytest.mark.run(order=215)
    def test_ProfessionRecordStatistics(self,driver,Data):
        """执业备案统计"""
        self.assert_result = all(driver,Data).test_ProfessionRecordStatistics()

    # @pytest.mark.test
    @pytest.mark.role_association
    @pytest.mark.parametrize("Data",ExcelData("test_LicenseImportTrack_01"))
    @pytest.mark.run(order=216)
    def test_LicenseImportTrack(self,driver,Data):
        """导入数据统计：所有的操作"""
        self.assert_result = all(driver,Data).test_LicenseImportTrack_01()