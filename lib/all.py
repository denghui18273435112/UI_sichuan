import time
import traceback
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium
from config.fixed_options import *
import json
from config.path import *
import time
import pytest
from PIL import Image
from selenium import webdriver
from tools.Base import *
from tools.Yaml_read import Yaml_read
from tools.selenium import selenium
import os
from config.Conf import _file_path
from tools.verification_code import verification_code
from config.path import *
class all:
    def __init__(self,driver,Data):
        self.driver = selenium(driver)
        self.data = json.loads(Data["data"])
        self.ExcelData = Data
        self.driver.url_skip(self.ExcelData["URL"])
        print("\n{} 运行中.....".format(self.ExcelData["test_id"]))
        time.sleep(5)

    def overview_digital(self):
        """"数字概览：饼图统计"""
        try:
            self.driver.click("数字概览","contains_text")
            self.driver.click("div  div.top > div:nth-child(2) > div span>span")
            self.driver.click("//li/span[contains(text(),'线上')]",type="xpath")
            #总已参训人数/总计划人数
            CXJHZRS=self.driver.text_get("div:nth-child(1) > div > div.container  span:nth-child(1) > span.total")
            ZYCXRS1 = int(CXJHZRS.split("/")[0])
            ZJHRS = int(CXJHZRS.split("/")[1])
            CL=int(self.driver.text_get("div:nth-child(1) > div > div.container  span:nth-child(2) > span.value"))
            ZL=int(self.driver.text_get("div:nth-child(1) > div > div.container  span:nth-child(3) > span.value"))
            YCX=int(self.driver.text_get("div:nth-child(1) > div > div.container  span:nth-child(4) > span.value"))
            WCX=int(self.driver.text_get("div:nth-child(1) > div > div.container  span:nth-child(5) > span.value"))
            if  YCX !=0:
                #总达标人数/总参训人数
                ZDBZCX = self.driver.text_get("div:nth-child(2) > div > div.container  span:nth-child(1) > span.total")
                ZDBRS = int(ZDBZCX.split("/")[0])
                ZYCXRS2 = int(ZDBZCX.split("/")[1])
                YDB=int(self.driver.text_get("div:nth-child(2)  div.container  span:nth-child(2) > span.value"))
                WDB=int(self.driver.text_get("div:nth-child(2)  div.container  span:nth-child(3) > span.value"))
                if ZYCXRS1==YCX and ZJHRS==(CL+ZL) and ZDBRS==YDB and ZYCXRS2==(YDB+WDB):
                    self.ExcelData["expected_result"] = "总已参训人数:{0};总计划人数:{1};存量:{2};增量:{3};已参训:{4};未参训:{5};" \
                        "总达标人数:{6};总已参训人数:{7};已达标:{8};未达标:{9};".format(ZYCXRS1,ZJHRS,CL,ZL,YCX,WCX,ZDBRS,ZYCXRS2,YDB,WDB)
                else:
                    self.ExcelData["actual_result"] = False
            else:
                self.ExcelData["actual_result"] = "当前线上第三方没有数据,怀疑数据异常"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def standard_direction(self):
        """数字概览：参训/达标走势图"""
        try:
            self.driver.click("数字概览","contains_text")
            self.driver.click("div  div.top > div:nth-child(2) > div span>span")
            self.driver.click("//li/span[contains(text(),\"线上\")]",type="xpath")
            self.driver.click("#app > div > div.container.main-right.scroll-bar > div.wrapper")
            self.driver.click("#app > div > div.container.main-right.scroll-bar")
            self.driver.Page_scrolling(5000,Positioning_way="ClassName")
            self.driver.click("div.wrapper > div.line div.right-wrapper > div > span.chart.active")
            self.driver.click("div.condition.conditions > div.right-wrapper > div > span.tables")
            self.driver.screenShots()
            if  self.driver.list_data_number("div.is-scrolling-none>table.el-table__body>tbody") >=1:
                self.driver.click("div.right-wrapper > div:nth-child(1) > span")
                self.driver.click("div.right-wrapper > div:nth-child(2) > span.chart")
                self.driver.click("div.left-wrapper > div:nth-child(1) div > span > span > i")
                self.driver.click("//li/span[contains(text(),\"达标走势\")]",type="xpath")
            else:
                self.ExcelData["actual_result"] = "当前参训/达标走势图 列表无数据"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def kinds_standards(self):
        """数字概览：各类达标情况"""
        try:
            self.driver.click("数字概览","contains_text")
            self.driver.Page_scrolling(Positioning_way="ClassName")
            ke_shuliang = self.driver.list_data_number(location="div > div.wrapper > div.pies > div:nth-child(2) > div",location_type1="span")
            if ke_shuliang >=1:
                CXJHZRS=self.driver.text_get("div:nth-child(1) > div > div.container  span:nth-child(1) > span.total")
                ZYCXRS = int(CXJHZRS.split("/")[0])
                sum_new = 0
                dingwei = self.driver.text_get("div.pies > div:nth-child(2)  div:nth-child(1) > div > span:nth-child(1)").split("/")[0].split(":")[1]
                sum_new += int(dingwei)
                if  sum_new>=1:
                    self.ExcelData["expected_result"] = "只能证明有数据而已；课程的数据：{}".format(ke_shuliang//2)
                else:
                    self.ExcelData["actual_result"] = False
            else:
                self.ExcelData["actual_result"] = "当前统计处没有课程"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def student_details(self):
        """学员详情：字段查询"""
        try:
            self.driver.click("学员详情","contains_text")
            time.sleep(2)
            if  self.driver.list_data_number() >=1:
                #培训类型/岗前测评完成状态/达标状态
                training_type = self.driver.text_get(6,"zzl_list_01")
                self.driver.drop_down_choice(3,training_type,type1="css_1",type2="xpath_1")
                if  self.driver.list_data_number() >0:
                    for y in range(1,self.driver.list_data_number()+1):
                        if  self.driver.text_get(10,"zzl_list_01",y) != "--":
                            gangqian_type = self.driver.text_get(10,"zzl_list_01",y)
                            break
                self.driver.drop_down_choice(5,gangqian_type,type1="css_1",type2="xpath_1")
                dabiao_type =self.driver.text_get(13,"zzl_list_02")
                self.driver.drop_down_choice(4,dabiao_type,type1="css_1",type2="xpath_1")
                for x in range(1,self.driver.list_data_number()):
                    if  dabiao_type not in  self.driver.text_get(13,"zzl_list_02",x)\
                            and training_type not in  self.driver.text_get(6,"zzl_list_01",x)\
                            and gangqian_type  not in  self.driver.text_get(10,"zzl_list_01",x):
                        self.ExcelData["actual_result"] = "筛选条件和返回结果不一致"
                self.driver.click("导出",type="contains_text")
                XM = self.driver.text_get(2,"zzl_list_01")
                ZJHM = self.driver.text_get(3,"zzl_list_01")
                self.driver.click(14,"zzl_list_02")
                NEW_XM = self.driver.text_get(" div.el-row > div:nth-child(1) > span").split("：")[1]
                NEW_ZJHM = self.driver.text_get(" div.el-row > div:nth-child(3) > span").split("：")[1]
                if  XM!=NEW_XM and ZJHM!=NEW_ZJHM:
                    self.ExcelData["actual_result"] = "列表与详情呈现不一致"
                self.driver.screenShots("培训类型、岗前测评完成状态、达标状态查询")
                self.driver.click("div.title>span:nth-child(2)>svg")
                # 公司名称/姓名、证件号码
                name = self.driver.text_get(2,"zzl_list_01")
                number_id = self.driver.text_get(3,"zzl_list_01")
                self.driver.text_input("div.condition-item:nth-child(1) div > input",name)
                self.driver.text_input("div.condition-item:nth-child(2) div > input",number_id,Enter=True)
                if name not in self.driver.text_get(2,"zzl_list_01") and  number_id not in self.driver.text_get(3,"zzl_list_01"):
                    self.ExcelData["actual_result"] = "筛选条件和返回结果不一致"
                self.driver.screenShots("公司名称姓名、证件号码查询")
            else:
                self.ExcelData["actual_result"] = "当前查询列表无数据、模块数据异常、当前列表数据少于5条,无法开发自动化测试"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def company_data(self):
        """公司数据：查询导出"""
        try:
             self.driver.click("公司数据","contains_text")
             self.driver.click("div.top20.table-area > div.tabs > span.tables > svg")
             if  self.driver.list_data_number(location="div.is-scrolling-none>table>tbody",plural=0) >0 and self.driver.list_data_number(location="div.is-scrolling-none>table>tbody",plural=1) >0:
                 self.driver.click("div.top20.table-area > div.tabs > span.chart >svg")
                 self.driver.text_input("div.condition > div > div > div:nth-child(1) > div > input",
                                         self.driver.text_get(" table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center > div"),Enter=True)
                 self.driver.click("div.condition > div > div > div:nth-child(2) > span")
             else:
                self.ExcelData["actual_result"] = "列表数据数据;请手动确认此模块是否存在异常"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def tabulate_data(self):
        """汇总数据：查询"""
        try:
            self.driver.click("汇总数据","contains_text")
            time.sleep(5)
            if self.driver.list_data_number(location="div.is-scrolling-none>table>tbody") ==0:
                self.ExcelData["actual_result"] =="列表数据数据;请手动确认此模块是否存在异常"
            # CXRS = self.driver.text_get("tbody  tr td:nth-child(2) div")
            # if int(CXRS)!=0:
            #     self.ExcelData["actual_result"] =="有数据没问题"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def PlanSubmit_01(self):
        """培训计划报送：填写报送计划"""
        try:
            if self.driver.list_data_number(location="table.el-table__body>tbody", plural=0) ==22:
                self.driver.click("div:nth-child(5) > span.zzl-button")
                self.driver.click("div:nth-child(7) > span.zzl-button")
                self.driver.click("确定",type="contains_text")
            else:
                self.ExcelData["actual_result"] = "当前列表的数据条数不足22条"
       #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def PlanSubmit_02(self):
        """培训计划报送：操作退回"""
        try:
            if self.driver.list_data_number("div.el-table__fixed-body-wrapper>table>tbody") >1:
                self.driver.click("div.condition>div:nth-child(7)")
                self.driver.text_input("input[placeholder=\"请选择所属机构\"]",self.data["company"],type="css",empty=True)
                self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li")
                self.driver.click("div:nth-child(5) > span.zzl-button")
                self.driver.click("div:nth-child(8) > span.zzl-button")
            else:
                self.ExcelData["actual_result"] ==self.ExcelData["location_fail_hint"]
       #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def query_inquire(self):
        """培训记录查询模块-查询、按钮操作"""
        try:
            if self.driver.list_data_number() >0:
                self.driver.text_input("input[placeholder='请选择所属机构']",self.driver.text_get(1,"zzl_list_01"),empty=True)
                self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)")
                self.driver.drop_down_choice(2,"仅限本机构",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(2,"本机构及下级",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(4,self.driver.text_get(6,"zzl_list_01"),type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(3,"2022",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(3,"2021",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(7,"身份证",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(9,"线上",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(10,"其他第三方",type1="css_1",type2="xpath_1")
                # self.driver.resfresh()
                self.driver.click("重置",type="starts_with_1")
                self.driver.text_input("div:nth-child(6) > div.el-input > input[placeholder=\"请输入\"]",self.driver.text_get(2,"zzl_list_01"))
                self.driver.text_input("div:nth-child(8) > div.el-input > input[placeholder=\"请输入\"]",self.driver.text_get(4,"zzl_list_01"))
                self.driver.click("查询",type="starts_with_1")
                self.driver.click("导出",type="starts_with_1")
                self.driver.text_input("//*/span[starts-with(.,\"前往\")]//input",10,type="xpath")
            else:
                self.ExcelData["actual_result"] =="当前列表无数据，可能存在数据异常"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def inquire_operation(self):
        """培训学分查询模块-字段查询"""
        try:
            if self.driver.list_data_number() >0:
                self.driver.text_input("input[placeholder='请选择所属机构']",self.driver.text_get(1,"zzl_list_01"),empty=True)
                self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)")
                self.driver.drop_down_choice(2,"仅限本机构",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(2,"本机构及下级",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(4,self.driver.text_get(6,"zzl_list_01"),type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(3,"2020",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(3,"2021",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(7,"身份证",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(9,"线上",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(10,"其他第三方",type1="css_1",type2="xpath_1")
                self.driver.click("重置",type="starts_with_1")
                self.driver.text_input("div:nth-child(6) > div.el-input > input[placeholder='请输入']",self.driver.text_get(2,"zzl_list_01"))
                self.driver.text_input("div:nth-child(8) > div.el-input > input[placeholder='请输入']",self.driver.text_get(4,"zzl_list_01"))
                self.driver.click("查询",type="starts_with_1")
                self.driver.click("导出",type="starts_with_1")
                self.driver.text_input("//*/span[starts-with(.,'前往')]//input",10,type="xpath",empty=True)
            else:
                self.ExcelData["actual_result"] =="当前列表无数据，可能存在数据异常"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def account_management_inquire(self):
        """账号管理-查询/按钮操作"""
        try:
            time.sleep(15)
            # self.driver.drop_down_choice(2,self.data["category"],type1="css_1",type2="xpath_1")
            # self.driver.drop_down_choice(3,self.data["state"],type1="css_1",type2="xpath_1")
            # self.driver.drop_down_choice(4,self.data["login_state"],type1="css_1",type2="xpath_1")
            # self.driver.text_input("请输入昵称",self.data["name"],type="css_1")
            self.driver.click("查询",type="starts_with_1")
            self.driver.click("导出",type="starts_with_1")
            # self.driver.text_input("//*/span[starts-with(.,'前往')]//input",10,type="xpath",empty=True)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def test_account_management_add(self):
        """账号管理-账号添加"""
        try:
            time.sleep(15)
            self.driver.click("div.table-area div.export>span:nth-child(3)")
            self.driver.text_input("请输入用户名",self.data["user"],type="css_1")
            self.driver.text_input("请输入用户昵称",self.data["nickname"],type="css_1")
            self.driver.text_input("请输入手机号",self.data["mobile"],type="css_1")
            self.driver.text_input("请输入新密码",self.data["password"],type="css_1")
            self.driver.text_input("再次输入密码",self.data["password"],type="css_1")
            self.driver.text_input("div.content > div > form > div > div.el-col.el-col-24 > div > div > div > div > input",self.data["company"])
            self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li",plural=1)
            self.driver.click("确定",type="starts_with_1")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def test_account_management_delete(self):
        """账号管理-账号删除"""
        try:
            time.sleep(15)
            for x in range(1,10):
                name = self.driver.text_get("div.el-table__body-wrapper tbody>tr:nth-child({0})>td:nth-child(2)".format(x))
                if name ==self.data["delete_user"]:
                    self.driver.click("div.el-table__body-wrapper tbody>tr:nth-child({})>td:nth-child(1)".format(x))
                    self.driver.click("批量删除",type="contains_text")
                    self.driver.click("确定",type="contains_text")
                    break
                else:
                    self.ExcelData["actual_result"] = "尚未找到需要删除的用户信息"
         #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_RecordImport(self):
        """培训记录导入：省公司导入数据"""
        try:
            self.driver.click("寿险模板",type="contains_text")
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_03,plural=0,type="input")
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_04,plural=1,type="input")
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_04,plural=2,type="input")
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_04,plural=3,type="input")
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_04,plural=4,type="input")
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_04,plural=5,type="input")
            self.driver.text_input("div:nth-child(1) > div:nth-child(1) > div > div > div > input",self.data["add_name"])
            self.driver.text_input("div:nth-child(1) > div:nth-child(4) > div > div > div > input","测试数据2")
            self.driver.text_input("div:nth-child(1) > div:nth-child(3) > div > div > div > input","测试数据3",plural=1)
            self.driver.text_input("div:nth-child(1) > div:nth-child(5) > div > div > div > input","测试数据4")
            self.driver.click("选择课程大纲",type="contains_text")
            self.driver.drop_down_choice(" div:nth-child(1) > div:nth-child(1) > div > div > span > span > i","B类：商业非车险执业合规培训",type2="contains_text_2")
            self.driver.drop_down_choice(" div:nth-child(1) > div:nth-child(2) > div > div > span > span > i","信用保证保险",type2="contains_text_2")
            for x in range(1,10):
                self.driver.click("label:nth-child({}) > span.el-checkbox__input > span".format(x))
            self.driver.click("确定",type="contains_text")
            self.driver.text_input("div:nth-child(1) > div:nth-child(2)  div > input:nth-child(2)","2022-01-01 00:00:00",plural=0)
            self.driver.text_input("div:nth-child(1) > div:nth-child(2)  div> input:nth-child(4)","2022-01-01 00:00:00")
            self.driver.click("提交",type="contains_text",plural=1)
            time.sleep(5)
         #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def test_CreditInquire(self):
        """培训记录统计-字段查询、按钮操作"""
        try:
            # self.driver.text_input("input[placeholder='请选择所属机构']",self.data["company"],empty=True)
            # self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)")
            self.driver.drop_down_choice(5,"本机构",type1="css_1",type2="xpath_1")
            self.driver.drop_down_choice(5,"其他第三方",type1="css_1",type2="xpath_1")
            self.driver.drop_down_choice(2,"2020",type1="css_1",type2="xpath_1")
            self.driver.drop_down_choice(2,"2021",type1="css_1",type2="xpath_1")
            self.driver.drop_down_choice(4,"线上",type1="css_1",type2="xpath_1")
            self.driver.click("导出",type="starts_with_1")
            #self.driver.drop_down_choice(4,"全部",type1="css_1",type2="xpath_1",plural2=3)
            self.driver.click("导出",type="starts_with_1")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def test_TrainingFileManage(self):
        """培训档案管理：删除数据"""
        try:
            self.driver.click("导出",type="starts_with_1")
            self.driver.drop_down_choice(2,"2020",type1="css_1",type2="xpath_1")
            self.driver.drop_down_choice(2,"2021",type1="css_1",type2="xpath_1")
            self.driver.click("重置",type="starts_with_1")
            for x in range(1,10):
                name = self.driver.text_get("div.el-table__body-wrapper tbody>tr:nth-child({0})>td:nth-child(4)".format(x))
                if name ==self.data["delete_name"]:
                    self.driver.click("div.el-table__body-wrapper tbody>tr:nth-child({})>td:nth-child(1)".format(x))
                    self.driver.click("审核",type="contains_text",plural=4)
                    self.driver.click("通过",type="contains_text")
                    self.driver.back()
                    break
                else:
                    self.ExcelData["actual_result"] = "尚未找到需要删除的用户信息"
            # self.driver.drop_down_choice(4,"审核拒绝",type1="css_1",type2="xpath_1")
            # time.sleep(3)
            # for x in range(1,10):
            #     name = self.driver.text_get("div.el-table__body-wrapper tbody>tr:nth-child({0})>td:nth-child(4)".format(x))
            #     if name ==self.data["delete_name"]:
            #         self.driver.click("div.el-table__body-wrapper tbody>tr:nth-child({})>td:nth-child(1)".format(x))
            #         self.driver.click("删除",type="contains_text")
            #         self.driver.click("确定",type="contains_text")
            #         self.driver.click("导出",type="starts_with_1")
            #         break
            #     else:
            #         self.ExcelData["actual_result"] = "尚未找到需要删除的用户信息"
            time.sleep(3)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def test_OnlineLearning(self):
        """在线学习-查看一下"""
        try:
            time.sleep(5)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def test_TrainingExam_01(self):
        """培训测评-培训测评 查询操作"""
        try:
            self.driver.click("培训测评","contains_text",plural=1)
            time.sleep(10)
            if self.driver.list_data_number() >0:
                self.driver.text_input("input[placeholder='请选择所属机构']",self.driver.text_get(1,"zzl_list_01"),empty=True)
                self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)")
                self.driver.drop_down_choice(2,"仅限本机构",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(2,"本机构及下级",type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(7,self.driver.text_get(6,"zzl_list_01"),type1="css_1",type2="xpath_1")
                self.driver.drop_down_choice(3,"2020",type1="css_1",type2="xpath_1",plural1=0)
                self.driver.drop_down_choice(3,"2021",type1="css_1",type2="xpath_1",plural1=0)
                self.driver.drop_down_choice(5,"身份证",type1="css_1",type2="xpath_1",plural1=0)
                self.driver.text_input("div:nth-child(4) > div.el-input > input[placeholder='请输入']",self.driver.text_get(2,"zzl_list_01"))
                self.driver.text_input("div:nth-child(6) > div.el-input > input[placeholder='请输入']",self.driver.text_get(4,"zzl_list_01"))
                self.driver.click("查询",type="starts_with_1")
                self.driver.click("导出",type="starts_with_1")
                self.driver.text_input("//*/span[starts-with(.,'前往')]//input",10,type="xpath",empty=True)
                self.driver.click("模板下载",type="starts_with_1")
                #self.driver.upload_file("批量导入查询",file_path_05,location_type="contains_text",type="no_input")
                self.driver.upload_file("div:nth-child(8) > div > div > input",file_path_05,type="input")
                time.sleep(5)
            else:
                self.ExcelData["actual_result"] = "列表无数据"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_TrainingExam_02(self):
        """培训测评-培训统计 查询操作"""
        try:
            self.driver.click("培训统计","contains_text")
            time.sleep(10)
            self.driver.text_input("请输入机构名称查询",self.driver.text_get(1,"zzl_list_01"),type="css_1",Enter=True)
            self.driver.click("查询",type="starts_with_1")
            self.driver.click("导出",type="starts_with_1")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData



    def test_logion_fail(self):
        """账号登录：失败"""
        try:
            login =Yaml_read("all_data.yaml","login")
            time.sleep(10)
            self.driver.text_input("请输入账号",self.data["user"],type="css_1")
            self.driver.text_input("请输入密码",self.data["password"],type="css_1")
            while True:
                #截图验证并设别；直到验证码正常位置
                element =self.driver.click('form  img')
                self.driver.text_input("请输入验证码","eeee",type="css_1")
                self.driver.click("span.login-button")
                if self.driver.get_url() !=login["login_contrast_url"]:
                    break
                else:
                    self.ExcelData["actual_result"] = "错误的验证也可以登录"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_logion_succeed(self):
        """账号登录：成功"""
        try:
            login =Yaml_read("all_data.yaml","login")
            time.sleep(10)
            self.driver.text_input("请输入账号",self.data["user"],type="css_1")
            self.driver.text_input("请输入密码",self.data["password"],type="css_1")
            self.driver.text_input("请输入验证码","denghui",type="css_1")
            # while True:
            #     # #截图验证并设别；直到验证码正常位置
            #     # element =self.driver.click('form  img')
            #     # left = int(element.location['x'])
            #     # top = int(element.location['y'])
            #     # right = int(element.location['x'] + element.size['width'])
            #     # bottom = int(element.location['y'] + element.size['height'])
            #     # path = _file_path + os.sep + 'code.png'
            #     # self.driver.save_screenshot(path)
            #     # im = Image.open(path)
            #     # im = im.crop((left, top, right, bottom))
            #     # im.save(path)
            #     # print("\n识别的验证码:{}\n".format(verification_code()))
            #     self.driver.text_input("请输入验证码","denghui",type="css_1")
            #     self.driver.click("span.login-button")
            #     if self.driver.get_url() ==login["login_contrast_url"]:
            #         pass
            #     else:
            #         self.ExcelData["actual_result"] = "登录失败"

            time.sleep(10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

######################################################诚信相关模块###############################################################################
    def OD_inquire(self):
        """个人信息查询-单个查询"""
        try:
            self.driver.text_input(location="请输入姓名",content=self.data["name"],type="css_1")
            self.driver.drop_down_choice(location1="div:nth-child(2) > div.el-select  span > i", location2=self.data["type"], type2="starts_with")
            self.driver.text_input(location="请输入证件号码",content=self.data["number"],type="css_1",Enter=True)
            if  self.ExcelData["actual_result"] != "test_OD_inquire_05":
                if  self.driver.list_data_number("div.is-scrolling-left>table.el-table__body>tbody") >=1:
                    name = self.driver.text_get(1,type="zzl_list_01")
                    type = self.driver.text_get(8,type="zzl_list_01")
                    number = self.driver.text_get(9,type="zzl_list_01")
                    if name == self.data["name"] and  type == self.data["type"] and  number == self.data["number"]:
                        self.driver.click(16,"zzl_list_02")
                        self.driver.back()
                    else:
                        self.ExcelData["actual_result"] = "条件查询与列表渲染数据不一致"
            else:
                if  self.driver.text_get("div.el-message>p")!="查询条件无对应数据":
                    self.ExcelData["actual_result"] = "没有弹出提示信息"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def Batch_query_Reset(self):
        """个人信息查询-批量查询、重置"""
        try:
            self.driver.click("div.condition div:nth-child(6)")
            self.driver.text_input("div.container textarea", self.data["nameORnumber"])
            self.driver.click("div.container div.footer span:nth-child(2)")
            if  self.driver.list_data_number("div.is-scrolling-left>table.el-table__body>tbody") !=4:
                self.ExcelData["actual_result"] = "当前查询列表无数据"
            self.driver.screenShots()
            self.driver.click("div.condition span.zzl-button",plural=1)
            if  self.driver.list_data_number("div.is-scrolling-left>table.el-table__body>tbody") !=0:
                self.ExcelData["actual_result"] = "当前查询列表渲染数据"
            self.driver.screenShots()
       #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def import_query(self):
        """导入批量查询"""
        try:
            self.driver.click("模板下载",type="contains_text")
            self.driver.upload_inputType("div:nth-child(2) div > div:nth-child(8)  input",file_path_02)
            time.sleep(5)
            self.driver.click("导出",type="contains_text")
            if  self.driver.list_data_number("div.is-scrolling-left>table.el-table__body>tbody") !=4:
                self.ExcelData["actual_result"] = "当前查询列表无数据"
       #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def IPM_query(self):
        """单个查询"""
        try:
            self.driver.text_input(location="div.condition-wrapper > div > div:nth-child(2) > div.el-input>input",content=self.data["name"])
            self.driver.text_input(location="div.condition-wrapper > div > div:nth-child(4) > div.el-input>input",content=self.data["number_id"])
            self.driver.text_input(location="div.condition-wrapper > div > div:nth-child(5) > div.el-input>input",content=self.data["PC"])
            self.driver.click("div.condition-wrapper div:nth-child(18)")
            #self.driver.click("div.el-table__header-wrapper> table.el-table__header tr>th:nth-child(1) label")
            self.driver.click("div.condition-wrapper div:nth-child(20)")
            self.driver.click("div.condition-wrapper div:nth-child(21)")
            self.driver.click("div.condition-wrapper div:nth-child(24)")
            self.driver.text_input("div.container textarea", self.data["number_id"])
            self.driver.click("body > div:nth-child(17) > div > div.el-dialog__body > div > div.footer > span.zzl-button.primary")

       # #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except Exception:
            traceback.print_exc()
            #print(traceback.print_exc())
            self.ExcelData["actual_result"] = self.ExcelData["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.ExcelData)
        print("{} 已结束.....".format(self.ExcelData["test_id"]))
        return self.ExcelData["actual_result"]

    def Default_condition_query(self):
        """多模块默认条件查询"""
        try:
            if self.ExcelData["test_id"] == "test_Default_condition_query_01":
                self.driver.click("div.condition-wrapper > div > div:nth-child(18)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_02":
                self.driver.click("确定",type="starts-with")
                self.driver.click("div > div.condition-wrapper > div > div:nth-child(9)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_03":
                self.driver.click("查询",type="starts-with")
                time.sleep(5)
            elif self.ExcelData["test_id"] == "test_Default_condition_query_05":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_09":
                self.driver.click("div.top-tabs span:nth-child(1)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_10":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_11":
                self.driver.click("div.top-tabs span:nth-child(3)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_12":
                self.driver.click("div.top-tabs span:nth-child(4)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_17":
                self.driver.click("div.top-tabs span:nth-child(1)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_18":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_20":
                self.driver.click("div.top-tabs span:nth-child(1)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_21":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_22":
                self.driver.click("div.top-tabs span:nth-child(3)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_23":
                self.driver.click("div.top-tabs span:nth-child(1)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_24":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_25":
                self.driver.click("div.top-tabs span:nth-child(1)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_26":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_28":
                self.driver.click("div.top-tabs span:nth-child(1)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_29":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_30":
                self.driver.resfresh()
                self.driver.click("div.top-tabs span:nth-child(1)")
                self.driver.click("div.condition-wrapper span.zzl-button.primary")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_31":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_32":
                self.driver.click("div.top-tabs span:nth-child(3)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_33":
                self.driver.click("div.top-tabs span:nth-child(4)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_36":
                self.driver.click("div.top-tabs span:nth-child(1)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_37":
                self.driver.click("div.top-tabs span:nth-child(2)")
            elif self.ExcelData["test_id"] == "test_Default_condition_query_39":
                pass
            else:
                self.driver.click("div.condition-wrapper span.zzl-button.primary")
            time.sleep(3)
       # #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except Exception:
            print(traceback.print_exc())
            self.ExcelData["actual_result"] = self.ExcelData["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.ExcelData)
        print("{} 已结束.....".format(self.ExcelData["test_id"]))
        return self.ExcelData["actual_result"]

    def record_statistical_query_inquire(self):
        """培训记录统计模块-查询-操作"""
        try:
            print("培训记录统计模块-查询-操作 中.....")
            self.driver.zzl_company_inquire("中国人民财产保险股份有限公司广东省分公司")
            self.driver.zzl_pull_down_inquire(2,"2020")
            self.driver.zzl_pull_down_inquire(4,"线下")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_pull_down_inquire(4,"线上")
            self.driver.zzl_pull_down_inquire(5,"本机构")
            #self.driver.zzl_pull_down_inquire(7,"已达标")
            #self.driver.resfresh()
            self.driver.zzl_click("查询",type="xpath_starts-with")
            self.driver.zzl_click("重置",type="xpath_starts-with")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_text_input("//*/span[starts-with(.,\"前往\")]//input",10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        print("培训记录统计模块-查询-操作 已结束")
        return self.Data["actual_result"]


    def test_IncumbentImport(self):
        """在职人员管理-导入页面：导入操作"""
        try:
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_06,type="input")
            time.sleep(10)
            if self.driver.list_data_number() !=1:
                self.ExcelData["actual_result"] = "列表没有渲染错误的失败信息"
            self.driver.screenShots()
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_LeaversImport(self):
        """离职人员管理-导入页面：导入操作"""
        try:
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_07,type="input")
            if self.driver.list_data_number("div.el-table__body-wrapper>table>tbody") !=1:
                self.ExcelData["actual_result"] = "列表没有渲染错误的失败信息"
            self.driver.screenShots()
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_update_01(self):
        """个人信息修改"""
        try:
            self.driver.click("个人信息修正","contains_text")
            self.driver.click("div.condition span",plural=6)
            self.driver.text_input("div.container textarea", self.data["nameORnumber"])
            self.driver.click("div.el-dialog__body span.zzl-button.primary:nth-child(2)")
            list_data_number = self.driver.list_data_number(location="div.el-table__body-wrapper > table > tbody")
            if  list_data_number >=4:
                self.driver.click("导出",type="contains_text")
                #进入个人档案和修改信息
                for x in range(1,list_data_number+1):
                    self.driver.click("div.el-table__fixed-body-wrapper tbody>tr:nth-child({})>td:nth-child(13) svg:nth-child(1)".format(x))
                    self.driver.back()
                    self.driver.click("div.el-table__fixed-body-wrapper tbody>tr:nth-child({})>td:nth-child(13) svg:nth-child(2)".format(x))
                    self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_10,plural=0,type="input")
                    self.driver.screenShots("图片上传")
                    self.driver.click("div.el-dialog__body  div.footer > span.primary",plural=1)
                    msg = self.driver.text_get("div.el-message>p",type="css_2")
                    if msg != "修改成功":
                        self.ExcelData["actual_result"] = "修改失败"
                    self.driver.screenShots("成功修改信息")
            else:
                self.ExcelData["actual_result"] = "当前列表没有数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_delete_data(self):
        """删除添加的数据"""
        try:
            time.sleep(0.5)
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_IncumbentManage(self):
        """在职人员管理"""
        try:
            #批量查询
            self.driver.click("批量查询",type="contains_text")
            self.driver.text_input("div.container textarea", self.data["nameORnumber"])
            self.driver.click("div.el-dialog__body span.zzl-button.primary:nth-child(2)")
            time.sleep(5)
            list_data_number =self.driver.list_data_number("div.is-scrolling-left.el-table__body-wrapper>table>tbody")
            get_list = []
            ExcelData_list = self.data["nameORnumber"].split("\n")
            if  list_data_number==2:
                self.driver.click("导出",type="contains_text")
                for x in range(1,list_data_number+1):
                    get_list.append(self.driver.text_get(location1=x,location=8,type="zzl_list_01"))
            if  ExcelData_list != get_list:
                self.ExcelData["actual_result"] = "列表数据不一致"
            self.driver.screenShots()
            #单个查询
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_LeaversManage(self):
        """离职人员管理"""
        try:
            self.driver.resfresh()
            time.sleep(2)
            self.driver.click("确定",type="contains_text")
            time.sleep(2)
            self.driver.text_input("div.condition-wrapper > div > div:nth-child(4) > div.el-input>input",content=self.data["nameORnumber"])
            self.driver.text_input("div.condition-wrapper > div > div:nth-child(2) > div.el-input>input",content=self.data["name"],Enter=True)
            if self.driver.list_data_number() ==1:
                self.driver.click("导出",type="contains_text")
                self.driver.click("div.el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td svg",plural=2)
                self.driver.back()
                self.driver.click("div.el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td svg",plural=3)
                self.driver.click("div.el-dialog__body  div.footer > span.primary",plural=1)
                self.driver.screenShots("成功修改信息")
            else:
                self.ExcelData["actual_result"]="查询无数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_EntryPersonInquiry(self):
        """入职人员查询"""
        try:
            self.driver.resfresh()
            time.sleep(2)
            self.driver.click("div.condition div:nth-child(14)")
            self.driver.text_input("div.container textarea", self.data["nameORnumber"])
            self.driver.click("提交",type="contains_text")
            data = self.driver.list_data_number("div.is-scrolling-left>table.el-table__body>tbody")
            if  data >=4:
                self.driver.click("导出",type="contains_text")
                for x in range(1,data+1):
                    self.driver.click("div.el-table__fixed-body-wrapper tbody>tr:nth-child({0})>td svg".format(x),plural=1)
                    self.driver.screenShots()
                    self.driver.back()
                    time.sleep(1)
            else:
                self.ExcelData["actual_result"]="查询无数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_OnJobPersonInquiry(self):
        """在职人员查询"""
        try:
            self.driver.resfresh()
            time.sleep(1)
            self.driver.click("div.condition div:nth-child(16)")
            self.driver.text_input("div.container textarea", self.data["nameORnumber"])
            self.driver.click("span.zzl-button.primary",plural=1)
            time.sleep(1)
            data = self.driver.list_data_number("div.is-scrolling-left>table.el-table__body>tbody")
            if  data >=2:
                self.driver.click("导出",type="contains_text")
                for x in range(1,data+1):
                    self.driver.click("div.el-table__fixed-body-wrapper tbody>tr:nth-child({0})>td svg".format(x),plural=1)
                    self.driver.screenShots()
                    self.driver.back()
                    time.sleep(1)
            else:
                self.ExcelData["actual_result"]="查询无数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_ResignPersonInquiry(self):
        """离职人员查询"""
        try:
            self.driver.resfresh()
            time.sleep(1)
            self.driver.click("div.condition div:nth-child(14)")
            self.driver.text_input("div.container textarea", self.data["nameORnumber"])
            self.driver.click("span.zzl-button.primary",plural=1)
            time.sleep(1)
            data = self.driver.list_data_number("div.is-scrolling-left>table.el-table__body>tbody")
            if  data >=2:
                self.driver.click("导出",type="contains_text")
                for x in range(1,data+1):
                    self.driver.click("div.el-table__fixed-body-wrapper tbody>tr:nth-child({0})>td svg".format(x),plural=1)
                    self.driver.screenShots()
                    self.driver.back()
                    time.sleep(1)
            else:
                self.ExcelData["actual_result"]="查询无数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_ProfessionRecordSend_01(self):
        """执业备案报送"""
        try:
            #零报告
            # self.driver.click("零报告",type="contains_text",plural=1)
            # self.driver.text_input("请输入报送人",type="css_1",content="自动化数据1206")
            # self.driver.text_input("请输入联系方式",type="css_1",content="18273435112")
            # self.driver.text_input("开始日期",type="css_1",content="2022-01-01",plural=1)
            # self.driver.text_input("结束日期",type="css_1",content="{}".format(time_YmdHMS(2)),plural=1,Enter=True)
            # self.driver.text_input("div.container textarea", "自动化数据")
            # self.driver.screenShots("零报告")
            # self.driver.click("添加",type="contains_text")
            #职业备案
            self.driver.click("div.condition>div:nth-child(7)")
            self.driver.text_input("请输入报送人",type="css_1",content="自动化数据1206")
            self.driver.text_input("请输入联系方式",type="css_1",content="18273435112")
            self.driver.text_input("开始日期",type="css_1",content="2022-01-01")
            self.driver.text_input("结束日期",type="css_1",content="{}".format(time_YmdHMS(2)),Enter=True)
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_08,plural=0,type="input")
            self.driver.upload_file(location="div.el-upload.el-upload--text>input",photo=file_path_09,plural=1,type="input")
            self.driver.screenShots("零报告")
            self.driver.click("div.btns > span.zzl-button.primary")
            #列表操作
            self.driver.resfresh()
            time.sleep(5)
            data = self.driver.list_data_number("div>table.el-table__body>tbody")
            if  data >=1:
                self.driver.click("导出",type="contains_text")
            else:
                self.ExcelData["actual_result"]="查询无数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_ProfessionRecordStatistics(self):
        """执业备案统计"""
        try:
            data = self.driver.list_data_number("div.table > div > div.is-scrolling-none > table > tbody")
            if  data >=1:
                self.driver.click("导出",type="contains_text")
            else:
                self.ExcelData["actual_result"]="查询无数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_ProfessionRecordSend_02(self):
        """执业备案报送"""
        try:
            self.driver.resfresh()
            data = self.driver.list_data_number("div>table.el-table__body>tbody")
            if  data >=2:
                self.driver.click("导出",type="contains_text")
                for x in range(1,data+1):
                    name =self.driver.text_get("div.el-table__body-wrapper tr:nth-child({0}) > td:nth-child(3) > div".format(x))
                    if name == "自动化数据1206":
                        self.driver.click("div.el-table__body-wrapper > table > tbody > tr:nth-child({0})>td:nth-child(8) span".format(x),plural=0)
                        self.driver.back()
                        self.driver.resfresh()
                        self.driver.click("div.el-table__body-wrapper > table > tbody > tr:nth-child({0})>td:nth-child(8) span".format(x),plural=1)
                        self.driver.click(" button.el-button--primary")
                        self.driver.screenShots("删除")
                        time.sleep(2)
                        break
            else:
                self.ExcelData["actual_result"]="查询无数据"
            #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData


    def test_LicenseImportTrack_01(self):
        """导入数据统计：所有的操作"""
        try:
            self.driver.click("导入数据统计",type="contains_text",plural=0)
            self.driver.click("div.condition div:nth-child(7)")
            self.driver.click("div.condition div:nth-child(6)")
            if self.driver.list_data_number("div.el-table__body-wrapper.is-scrolling-none>table>tbody")==2:
                self.driver.click("导出",type="contains_text")
                if self.driver.text_get(2,type="zzl_list_01") ==0 and  self.driver.text_get(3,type="zzl_list_01")==0:
                    self.ExcelData["actual_result"] = "列表报告数据异常"
            else:
                    self.ExcelData["actual_result"] = "列表数据异常"
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData

    def test_LicenseImportTrack_02(self):
        """执业证导入追踪：所有的操作"""
        try:
            self.driver.click("执业证导入追踪",type="contains_text",plural=2)
            self.driver.click("div.condition-wrapper  div:nth-child(4)")
            self.driver.click("div.condition-wrapper  div:nth-child(3)",plural=1)
            if self.driver.list_data_number("div.el-table__body-wrapper.is-scrolling-none>table>tbody")>=1:
                self.driver.click("导出",type="contains_text")
            else:
                    self.ExcelData["actual_result"] = "列表数据异常"
        except BaseException:
            traceback.print_exc()
            self.ExcelData["actual_result"] = traceback.format_exc()
        finally:
            return self.driver,self.ExcelData