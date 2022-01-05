import pytest
from tools.Yaml_read import Yaml_read
from lib.all import *
from tools.ExcelData import *

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



