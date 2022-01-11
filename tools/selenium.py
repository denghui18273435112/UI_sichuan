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

class selenium():
    def __init__(self,driver):
        """写一个构造函数，有一个参数driver
            # -> find_element("id","")
            # -> find_element("xpath","")
            # -> find_element("link text","")
            # -> find_element("partial link text","")
            # -> find_element("name","")
            # -> find_element("tag name","")
            # -> find_element("class name","")
            # -> find_element("css selector","")
        """
        self.driver= driver
    def find_element_by_css_selector(self):
        self.driver.find_element_by_css_selector()

    def save_screenshot(self,path):
        return self.driver.save_screenshot(path)

    def implicitly_wait(self, time):
       return self.driver.implicitly_wait(time)

    def send_keys(self,location,count):
        location.send_keys(count)

    def back(self):
        """浏览器后退按钮"""
        self.driver.back()

    def forward(self):
        """浏览器前进按钮"""
        self.driver.forward()

    def resfresh(self):
        """刷新页面"""
        self.driver.refresh()
        time.sleep(2)

    def open_url(self, url):
        """打开url站点"""
        self.driver.get(url)

    def quit_browser(self):
        """关闭并停止浏览器服务"""
        self.driver.quit()

    def clear(self,location):
        """清空文本数据"""
        location_new = self.driver.find_element_by_css_selector(location)
        location_new.clear()

    def get_url(self):
        """获取当前页面的url"""
        return self.driver.current_url

    def text_get(self, location, type="css",location1=1):
        """
        【用此方法】获取文本信息
        :return:
        """
        if type == "css":
            new_location = self.driver.find_element_by_css_selector(location)
        elif type == "xpath":
            new_location = self.driver.find_element_by_xpath(location)
        elif type == "zzl_list_01":#非悬浮
            new_location = self.driver.find_element_by_css_selector("div.el-table__body-wrapper tbody>tr:nth-child({0})>td:nth-child({1})".format(location1,location))
        elif type == "zzl_list_02":#悬浮
            new_location = self.driver.find_element_by_css_selector("div.el-table__fixed-body-wrapper tbody>tr:nth-child({0})>td:nth-child({1})".format(location1,location))
        return new_location.text

    def text_input(self,location,content,plural=None,Enter=False,empty=False,type="css"):
        """
        【用此方法】文本输入
        :param location: 定位
        :param content: 输入
        :param plural: 复数
        :param Enter:回车
        :param empty:清空
        :param type:类型
        :return:
        """
        if plural==None:
            if type == "id":
                text_frame = self.driver.find_element_by_id(location)
            elif type == "css":
                text_frame = self.driver.find_element_by_css_selector(location)
            elif type == "css_1":
                text_frame = self.driver.find_element_by_css_selector("input[placeholder='{0}']".format(location))
            elif type == "xpath":
                text_frame = self.driver.find_element_by_xpath(location)
            elif type == "xpath_starts_with":
                text_frame = self.driver.find_element_by_xpath("//*/span[starts-with(.,'{}')]".format(location))
            elif type == "xpath_contains_text":
                text_frame = self.driver.find_element_by_xpath("//li/span[contains(text(),'{}')]".format(location))
            elif type == "xpath_contains_text_1":
                text_frame = self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location))
            elif type == "xpath_contains_text_2":
                text_frame = self.driver.find_element(type,content)
        else:
            if type == "id":
                text_frame = self.driver.find_elements_by_id(location)[plural]
            elif type == "css":
                text_frame = self.driver.find_elements_by_css_selector(location)[plural]
            elif type == "css_1":
                text_frame = self.driver.find_elements_by_css_selector("input[placeholder='{0}']".format(location))[plural]
            elif type == "xpath":
                text_frame = self.driver.find_element_by_xpath(location)[plural]
            elif type == "xpath_starts_with":
                text_frame = self.driver.find_elements_by_xpath("//*/span[starts-with(.,'{}')]".format(location))[plural]
            elif type == "xpath_contains_text":
                text_frame = self.driver.find_elements_by_xpath("//li/span[contains(text(),'{}')]".format(location))[plural]
            elif type == "xpath_contains_text_1":
                text_frame = self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location))[plural]
        text_frame.click()
        time.sleep(1)
        if empty == True:
            text_frame.clear()
        text_frame.send_keys(content)
        if  Enter == True:
            text_frame.send_keys(Keys.ENTER)
            time.sleep(1)
        time.sleep(1)

    def drop_down_choice(self, location1, location2, plural1=None,plural2=None,type1="css", type2="css"):
        """【用此方法】下拉选择"""
        #点击
        if plural1==None:
            if type1 == "css":
                location1_new = self.driver.find_element_by_css_selector(location1)
            elif type1 == "css_1":
                location1_new = self.driver.find_element_by_css_selector("div div:nth-child({})>div.el-select>div>span".format(location1))
        else:
            if type1 == "css":
                location1_new = self.driver.find_elements_by_css_selector(location1)[plural1]
            elif type1 == "css_1":
                location1_new = self.driver.find_elements_by_css_selector("div div:nth-child({})>div.el-select>div>span".format(location1))[plural1]
        location1_new.click()
        time.sleep(1)
        #选择下拉数据
        if plural2==None:
            if type2 == "css":
                location2_new = self.driver.find_element_by_css_selector(location2)
            elif type2 == "xpath":
                location2_new = self.driver.find_element_by_xpath(location2)
            elif type2 == "xpath_1":
                location2_new = self.driver.find_element_by_xpath("//ul/li/span[contains(text(),'{}')]".format(location2))
            elif type2 == "starts_with":
                location2_new = self.driver.find_element_by_xpath("//*/span[starts-with(.,'{}')]".format(location2))
            elif type2 == "contains_text_1":
                location2_new = self.driver.find_element_by_xpath("//span[contains(text(),'{}')]".format(location2))
            elif type2 == "contains_text_2":
                location2_new = self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location2))
            location2_new.click()
            time.sleep(1)
        else:
            if type2 == "css":
                location2_new = self.driver.find_elements_by_css_selector(location2)[plural2]
            elif type2 == "xpath":
                location2_new = self.driver.find_elements_by_xpath(location2)[plural2]
            elif type2 == "xpath_1":
                location2_new = self.driver.find_elements_by_xpath("//ul/li/span[contains(text(),'{}')]".format(location2))[plural2]
            elif type2 == "starts_with":
                location2_new = self.driver.find_elements_by_xpath("//*/span[starts-with(.,'{}')]".format(location2))[plural2]
            elif type2 == "contains_text_1":
                location2_new = self.driver.find_elements_by_xpath("//span[contains(text(),'{}')]".format(location2))[plural2]
            elif type2 == "contains_text_2":
                location2_new = self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location2))[plural2]
            location2_new.click()
            time.sleep(1)

    def upload_file(self, location=None, photo=None,plural=None,location_type="css",type="input"):
        """
        【用此方法】上传文件
        @param location1: 定位图片上传位置
        @param photo: 图片文件的名称;直接传file下的文件名称即可
        """
        #非input类型
        if type!= "input":
            if plural == None:
                if location_type=="css":
                    location_new = self.driver.find_element_by_css_selector(location)
                elif location_type =="starts-with":
                    location_new = self.driver.find_element_by_xpath("//[starts-with(.,'{}')]".format(location))
                elif location_type == "contains_text":
                    location_new = self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location))
                elif location_type == "starts_with_1":
                    location_new = self.driver.find_element_by_xpath("//*/span[starts-with(.,'{}')]".format(location))
            else:
                if location_type=="css":
                    location_new = self.driver.find_elements_by_css_selector(location)[plural]
                elif location_type =="starts-with":
                    location_new = self.driver.find_element_by_xpath("//[starts-with(.,'{}')]".format(location))[plural]
                elif location_type == "contains_text":
                    location_new = self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location))[plural]
                elif location_type == "starts_with_1":
                    location_new = self.driver.find_element_by_xpath("//*/span[starts-with(.,'{}')]".format(location))[plural]
            location_new.click()
            time.sleep(2)
            browser_type="chrome"
            if browser_type.lower() == "chrome":
                title = "打开"
            elif browser_type.lower() == "firefox":
                title = "文件上传"
            elif browser_type.lower() == "ie":
                title = "选择要加载的文件"
            else:
                title = ""
            dialog = win32gui.FindWindow("#32770", title)
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
            comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)   # 三级
            edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
            button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, photo)  # 发送文件路径
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
            time.sleep(3)
        #input类型
        else:
            if plural == None:
                location_new1 = self.driver.find_element_by_css_selector(location)
            else:
                location_new1 =self.driver.find_elements_by_css_selector(location)[plural]
            location_new1.send_keys(photo)
        time.sleep(10)

    def switch_to(self):
        self.driver.switch_to.alert.text()

    def click(self, location,type="css",plural=None):
        """
        【用此方法】点击
        :param location: 定位
        """
        #非复数范畴
        if plural==None:
            if type =="starts-with":
                element = self.driver.find_element_by_xpath("//[starts-with(.,'{}')]".format(location))
            elif type == "contains_text":
                element = self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location))
            elif type == "starts_with_1":
                element = self.driver.find_element_by_xpath("//*/span[starts-with(.,'{}')]".format(location))
            elif type == "css":
                element = self.driver.find_element_by_css_selector(location)
            elif type == "css_1":
                element = self.driver.find_element_by_css_selector("input[placeholder='{}']".format(location))
            elif type == "xpath":
                element = self.driver.find_element_by_xpath(location)
            elif type == "figure":
                element = self.driver.find_element_by_css_selector("div:nth-child(2) > div.condition-wrapper  div:nth-child({0})".format(location))
            elif type == "zzl_list_01":#非悬浮框
                element = self.driver.find_element_by_css_selector("div.el-table__body-wrapper tbody>tr:nth-child(1)>td:nth-child({})".format(location))
            elif type == "zzl_list_02":#悬浮框
                element = self.driver.find_element_by_css_selector("div.el-table__fixed-body-wrapper tbody>tr:nth-child(1)>td:nth-child({})".format(location))
            element.click()
        #复数范畴
        elif plural!=None:
            if type =="starts-with":
                element = self.driver.find_elements_by_xpath("//[starts-with(.,'{}')]".format(location))[plural]
            elif type == "contains_text":
                element = self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location))[plural]
            elif type == "starts_with_1":
                element = self.driver.find_elements_by_xpath("//*/span[starts-with(.,'{}')]".format(location))[plural]
            elif type == "css":
                element = self.driver.find_elements_by_css_selector(location)[plural]
            elif type == "xpath":
                element = self.driver.find_elements_by_xpath(location)[plural]
            element.click()
        time.sleep(3)

    def screenShots(self, name_screenshot="截图"):
        """【用此方法】截图@param name_screenshot:截图名称或图片名称"""
        #截图并读取，写入进入allure报告中 file:切图文件的名称;name_screenshot:在allure中显示测试步骤标题; allure.attachment_type.PNG allure步骤的类型
        file_name=get_file_path_photo()+os.sep + "\\{}_{}.png".format(time_YmdHMS(), name_screenshot)
        self.driver.get_screenshot_as_file(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, name_screenshot+time_YmdHMS(), allure.attachment_type.PNG)

    def url_skip(self, name):
        """【用此方法】url拼接跳转"""
        login =Yaml_read("all_data.yaml","login")
        self.driver.get(login["joint_url"]+name)

    def Page_scrolling(self,Scroll_position=10000,plural=0,location="container",Scroll_type="no_windows",
                       Positioning_way="css",Scroll_way="Top"):
        """
        【用此方法】常见滚动
        :param Scroll_position: 滚动位置；100/200/1000
         :param plural: 复数
        :param location: 定位
        :param Positioning_way: 定位方式 id、ClassName、css
        :param Scroll_type: 滚动类型;windos滚动、table滚动、其它滚动
        :param Scroll_way: 滚动方式；左右上下 Top上下；Left左右
        :return:
        """
        if  Scroll_type== "no_windows":#非浏览器自带滚动条
            if  Positioning_way != "css":
                js = "var q=document.getElementsBy{0}('{1}')[{4}].scroll{3}={2}".format(Positioning_way, location, Scroll_position,Scroll_way,plural)
            elif Positioning_way =="css":
                js='document.querySelectorAll("{0}")[{1}].scroll{2}={3}'.format(location, plural,Scroll_way, Scroll_position)
        elif  Scroll_type== "windows":#浏览器自带滚动条
            js = "window.scrollTo(0,{})".format(Scroll_position)
        #print(js)
        self.driver.execute_script(js)

























    def jietu(self,filePath):
        """
        截图
        @param filePath:
        @parm file_path:截图后文件存放的位置
        @return:
        """
        file_path =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +os.sep+"file"
        self.driver.get_screenshot_as_file(get_file_path()+os.sep+filePath)




    def roll(self,location="right",up="500"):
        """
        仅限于页面自带的进度条
        location: tElementsByClassName定位
        @return:
        """
        self.driver.execute_script( 'document.getElementsByClassName("{}")[0].scrollTop={}'.format(location,up))
        time.sleep(0.5)


    def editor_upload_photo(self,location1="i.w-e-icon-image",location2="i.w-e-icon-upload2",photo="banner.png"):
        """
        编辑器中上传图片
        @param location1:定位编辑器图片上传位置
        @param location2: 定位图片上传位置
        @param photo: 图片文件的名称
        @return:
        """
        self.driver.implicitly_wait(10)
        location1_new = self.driver.find_element_by_css_selector(location1)
        location1_new.click()
        time.sleep(0.5)
        self.driver.implicitly_wait(10)
        location2_new = self.driver.find_element_by_css_selector(location2)
        location2_new.click()
        time.sleep(0.5)
        upload_files(photo)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)
        time.sleep(1)

    def FEBCS_CCSKK(self,location,content,enter=False):
        """
        定位-点击-清空-输入-隐性等待10S-回车
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.implicitly_wait(10)
        time.sleep(1)
        location_new = self.driver.find_element_by_css_selector(location)
        location_new.click()
        location_new.clear()
        location_new.send_keys(content)
        if enter==True:
            location_new.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.implicitly_wait(10)

    def input_text(self, location, content,fushu=None, Enter=None,type=None):
        """
        文本输入
       @param location: 文本定位
       @param content: 输入内容
       @param Enter: 是否回车；传入为0回车；Enter=None不回车
       @return:
       """
        time.sleep(1)
        if fushu ==None:
            self.driver.implicitly_wait(50)
            if '\u4e00' <= location <= '\u9fff':
                new_driver = self.driver.find_element_by_css_selector("input[placeholder=\"{0}\"]".format(location))
            elif ">" in location or "#" in location:
                new_driver = self.driver.find_element_by_css_selector(location)
            elif location.isalpha() == True:
                new_driver = self.driver.find_element_by_id(location)
            elif type =="xpath":
                new_driver = self.driver.find_element_by_xpath(location)
            new_driver.click()
            new_driver.clear()
            new_driver.send_keys(content)
            if Enter == 0:
                new_driver.send_keys(Keys.ENTER)
        else:
            self.driver.implicitly_wait(50)
            if '\u4e00' <= location <= '\u9fff':
                new_driver = self.driver.find_elements_by_css_selector("input[placeholder=\"{0}\"]".format(location))[fushu]
            elif ">" in location or "#" in location:
                new_driver = self.driver.find_elements_by_css_selector(location)[fushu]
            elif location.isalpha() == True:
                new_driver = self.driver.find_elements_by_id(location)[fushu]
            new_driver.click()
            new_driver.clear()
            new_driver.send_keys(content)
            if Enter == 0:
                new_driver.send_keys(Keys.ENTER)
        time.sleep(1)

    def send_key(self,content,Enter=None):
        """
        单纯输入
        :param Enter:
        :return:
        """
        self.driver.send_keys(content)
        if Enter == 0:
            self.driver.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)


    def test_input_id(self, location, content):
        """
        id类型的文本输入
        :param location:  id定位
        :param content:   输入的内容
        :return:
        """
        new_location = self.driver.find_element_by_id(location)
        new_location.click()
        new_location.clear()
        new_location.send_keys(content)

    def test_id(self, location):
        """
        id类型进行点击
        :param location:  id定位
        :return:
        """
        new_location = self.driver.find_element_by_id(location)
        new_location.click()

    def  text_data(self,location):
        """
        获取列表的文本数据
        :param location:位置
        :return:
        """
        return  self.driver.find_element_by_css_selector(location).text_get

    def select_pullDown_frame(self,location,option):
        """
        标准的select下拉框选项
        :param location:位置
        :param option:  根据索引、下拉框值
        :return:
        """
        if  option.isalpha() == True:
            Select(self.driver.find_element_by_css_selector(location)).select_by_visible_text(option)
        if isinstance(option,int) == True:
            Select(self.driver.find_element_by_css_selector(location)).select_by_index()


    def drop_down_box(self, location, location1, weizhi=None):
        """
        下拉框选择
        分两步：第一步点击弹出下拉框；第二步：选择下拉框选项
        备注：都支持复数
        @param location:第一步点击定位
        @param location1：下拉选项定位，下拉后的选项一般选择用xpath定位；css很难定位到
        @param weizhi: 第一步定位的位置
        @return:
        """
        time.sleep(1)
        if (">" in location or "." in location) and weizhi != None :
            self.driver.find_elements_by_css_selector(location)[int(weizhi)].click()
        elif (">" in location or "." in location) and weizhi == None :
            self.driver.find_element_by_css_selector(location).click()
        elif "/" in location  and weizhi != None :
            self.driver.find_element_by_xpath(location)[int(weizhi)].click()
        elif "/" in location  and weizhi == None :
            self.driver.find_element_by_xpath(location).click()
        elif '\u4e00' <= location <= '\u9fff' and weizhi != None:
            self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location))[int(weizhi)].click()
        elif '\u4e00' <= location <= '\u9fff' and weizhi == None:
            self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location)).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        if weizhi == None:
            if "/" in location1 or "//" in location1:
               self.driver.find_element_by_xpath(location1).click()
            elif '\u4e00' <= location1 <= '\u9fff':
                self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location1)).click()
                #self.driver.find_element_by_xpath("//*[text()=\"{}\"]".format(location1)).click()
            elif location1.isalpha() == True:
                self.driver.find_element_by_id(location1).click()
            elif ">" in location1:
                self.driver.find_element_by_css_selector(location1).click()
            self.driver.implicitly_wait(10)
            time.sleep(1)
        else:
            if "/" in location1 or "//" in location1:
               self.driver.find_elements_by_xpath(location1)[weizhi].click()
            elif '\u4e00' <= location1 <= '\u9fff':
                self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location1))[weizhi].click()
            elif location1.isalpha() == True:
                self.driver.find_elements_by_id(location1)[weizhi].click()
            elif ">" in location1:
                self.driver.find_elements_by_css_selector(location1)[weizhi].click()
            self.driver.implicitly_wait(10)
            time.sleep(1)

    def new_pull_down_choose(self,location,option_name,weizhi=None):
        """
        按钮点击；支持复数定位点击
        @param location:
        @param weizhi:
        @return:
        """
        time.sleep(1)
        if '\u4e00' <= location <= '\u9fff':
                new_driver = self.driver.find_element_by_css_selector("input[placeholder={}]".format(location)).click()
        if ">" in location or "=" in location:
                new_driver = self.driver.find_element_by_css_selector(location).click()
        if "/" in location:
                new_driver = self.driver.find_element_by_xpath(location).click()
        time.sleep(0.5)
        new_driver.select_by_visible_text(option_name)
        self.driver.implicitly_wait(10)
        time.sleep(1)

    def pull_down_choose_s(self, location, option_name):
        """
        下拉选择
        @param location:  定位下拉文本框位置
        @param option_name: 下拉选项名称
        @return:
       """
        if '\u4e00' <= location <= '\u9fff':
                self.driver.find_element_by_css_selector("input[placeholder={}]".format(location)).click()
        if ">" in location or "=" in location:
                self.driver.find_element_by_css_selector(location).click()
        if "/" in location:
                self.driver.find_element_by_xpath(location).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//span[contains(text(),"{0}")]'.format(option_name)).click()
        self.driver.implicitly_wait(10)





    def execute_script_new(self,shuxing,id,zhi):
        """
        更改页面属性
        :return:
        """
        if shuxing =="id":
            self.driver.execute_script('document.getElementById({0}).{1}'.format(id,zhi))

    def quit_iframe(self):
        """
        退出iframe嵌套网页 【常用之一】
        :return:
        """
        self.driver.switch_to.default_content()

    def nested_page(self,location):
        """
        进入iframe嵌套网页  【常用之一】
        嵌套页面;弹框;iframe窗口
        name属性、ID属性
        备注：没有可用的id或者name属性时
        可以先按照元素的定位方法，把frame找出来，再整体放到switch_to_frame()中
        内嵌网页后，需要有退出
        :param name:
        :return:
        """
        self.driver.switch_to.frame(location)

    def nested_page1(self,location):
        """
        进入iframe嵌套网页  【常用之一】
        嵌套页面;弹框;iframe窗口
        name属性、ID属性
        备注：没有可用的id或者name属性时
        可以先按照元素的定位方法，把frame找出来，再整体放到switch_to_frame()中
        内嵌网页后，需要有退出
        :param name:
        :return:
        """
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(location))

    def browser_pop_up(self,operation="YES",if_input=None):
        """
        浏览器自带的弹框操作 【常用之一】
        此类弹框无法用F12检测
        :param operation: YES 确认；NO 取消；TEXT 获取文本
        :return:
        """
        time.sleep(1)
        if operation =="YES":
            self.driver.switch_to.alert.accept()
        if operation == "NO":
            self.driver.switch_to.alter.dismisss()
        if operation == "TEXT":
            self.driver.switch_to.alert.text_get()
        if if_input !=None:
            self.driver.switch_to.alert.send_keys(operation)






    def JS(self,js):
        self.driver.execute_script(js)

    def click_two(self, location,location1):
        """
        两次点击  【常用之一:于下拉选项】
        :param location:
        :param location1:
        :return:
        """
        if "/" in location or "//" in location or "*" in location:
            self.driver.find_element_by_xpath(location).click()
        elif '\u4e00' <= location <= '\u9fff':
            self.driver.find_element_by_xpath("//li[contains(text(),'{}')]".format(location)).click()
        elif location.isalpha() == True:
            self.driver.find_element_by_id(location).click()
        elif ">" in location or "#" in location:
            self.driver.find_element_by_css_selector(location).click()
        if "/" in location1 or "//" in location or "*" in location1:
            self.driver.find_element_by_xpath(location1).click()
        elif '\u4e00' <= location1 <= '\u9fff':
            self.driver.find_element_by_xpath("//li[contains(text(),'{}')]".format(location1)).click()
        elif location1.isalpha() == True:
            self.driver.find_element_by_id(location1).click()
        elif ">" in location1 or "#" in location1:
            self.driver.find_element_by_css_selector(location1).click()



    def text_acquire(self, location=None,row="1",column=None):
        """
        文本获取

        :param location:
        :return:
        """
        self.driver.implicitly_wait(50)
        if  location!=None:
            dingwei = self.driver.find_element_by_css_selector(location)
        elif column!=None:
            dingwei = self.driver.find_element_by_css_selector("div.el-table__body-wrapper tbody>tr:nth-child({0})>td:nth-child({1})".format(row,column))
        return dingwei.text



    def pullDown_frame(self,location,option_name,label_name="li",matching_mode=True,joint=True):
        """
        下拉框选择  【常用之一】
        :param location:位置；方式CSS
        :param option_name：选项名称；方式：Xpath
        :param label_name:当前选项所在标签名称；默认：li
        :param matching_mode xpath的text方法支持包含匹配和精准匹配；默认包含匹配
        :param joint :是否对Xpath进行拼接
        :return:一般选项都放在 ul  li 标签上
        """
        self.driver.find_element_by_css_selector(location).click()
        if joint==True:
            if  matching_mode == True:
                self.driver.find_element_by_xpath("//{0}[contains(text(),'{1}')]".format(label_name,option_name)).click()
            else:
                self.driver.find_element_by_xpath("//{0}[text()='{1}']".format(label_name,option_name)).click()
        else:
                self.driver.find_element_by_xpath(option_name).click()



    def  time_current_YmdHMS(self):
        """
        返回年月日时分秒  【常用之一】
        :return:
        """
        return  str(datetime.now().strftime("%Y%m%d%H%M%S"))

    def  time_current_Ymd(self):
        """
        返回年月日时  【常用之一】
        :return:
        """
        return  str(datetime.now().strftime("%Y-%m-%d"))

    def  upload_inputType(self, location, content):
        """
        上传文件   【常用之一】 input 方式的文件上传;一般和标签同一级
        :param location: 位置
        :param content:  文件的绝对路径

        """
        self.driver.find_element_by_css_selector(location).send_keys(content)



#针对项目进行的封装
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def zzl_company_inquire(self, content, location="input[placeholder=\"请选择所属机构\"]"):
        """
        保险机构字段查询
        :param location:
        :param content:
        :return:
        """
        time.sleep(1)
        self.driver.implicitly_wait(20)
        new_location = self.driver.find_element_by_css_selector(location)
        new_location.click()
        new_location.clear()
        new_location.send_keys(content)
        time.sleep(1)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_css_selector("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)").click()
        time.sleep(1)
        self.driver.implicitly_wait(20)

    def zzl_company_inquire_s(self, content, location="input[placeholder=\"请选择所属机构\"]",type="css"):
        """
        保险机构字段选择
        :param location:
        :param content:
        :return:
        """
        time.sleep(1)
        self.driver.implicitly_wait(20)
        if type =="css":
            new_location = self.driver.find_element_by_css_selector(location)
        new_location.click()
        new_location.send_keys(content)
        time.sleep(2)
        self.driver.implicitly_wait(20)
        self.driver.find_elements_by_css_selector("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li")[1].click()
        time.sleep(2)
        self.driver.implicitly_wait(20)

    def zzl_pull_down_inquire(self,location1,location2,location1_type="css_zzl_1",location2_type="xpath_zzl_1"):
        """
        下拉框筛选
        :param location1: 第n个字段就写n
        :param location2:
        :return:
        """
        time.sleep(1)
        self.driver.implicitly_wait(20)
        if location1_type == "css_default":
            location1_click = self.driver.find_element_by_css_selector(location1)
        if location1_type == "css_zzl_1":
            location1_click = self.driver.find_element_by_css_selector("div div:nth-child({})>div.el-select>div>span".format(location1))
        location1_click.click()
        time.sleep(1)
        self.driver.implicitly_wait(20)
        if location2_type == "xpath_default":
            location2_click = self.driver.find_element_by_xpath(location2)
        if location2_type == "xpath_zzl_1":
            location2_click = self.driver.find_element_by_xpath("//ul/li/span[contains(text(),\"{}\")]".format(location2))
        location2_click.click()


    def zzl_text_input(self,location,content,Enter=True,empty=True,type="xpath"):
        """
        文本输入
        :param location: 定位
        :param content: 输入内容
        :param Enter:  文本框回车
        :param empty:  清空文本框中数据
        :param type:  定位的类型
        :return:
        """
        time.sleep(1)
        self.driver.implicitly_wait(20)
        if type == "id":
            text_frame = self.driver.find_elements_by_id(location)
        elif type == "css":
            text_frame = self.driver.find_element_by_css_selector(location)
        elif type == "xpath":
            text_frame = self.driver.find_element_by_xpath(location)
        elif type == "xpath_starts_with":
            text_frame = self.driver.find_element_by_xpath("//*/span[starts-with(.,'{}')]".format(location))
        elif type == "xpath_contains_text":
            text_frame = self.driver.find_element_by_xpath("//li/span[contains(text(),\"{}\")]".format(location))
        elif type == "css_text":
            text_frame = self.driver.find_element_by_css_selector("input[placeholder=\"{}\"]".format(location))
        elif location.isalpha() == True:
            text_frame = self.driver.find_element_by_css_selector(" div:nth-child({}) > div > input".format(location))
        text_frame.click()
        time.sleep(1)
        if empty == True:
            text_frame.clear()
        text_frame.send_keys(content)
        if  Enter == True:
            text_frame.send_keys(Keys.ENTER)
        time.sleep(1)



    def zzl_click(self, location,type="xpath"):
        """
        点击操作  【常用之一】
        :param location: 定位 ；支持方式:xpthon、id、css
        :return:
        """
        time.sleep(0.5)
        self.driver.implicitly_wait(20)
        if type =="xpath_starts-with":
            new_location = self.driver.find_element_by_xpath("//*/span[starts-with(.,\"{}\")]".format(location))
        if type == "xpath_contains_text":
            new_location = self.driver.find_element_by_xpath("//*/span[contains(text(),\"{}\")]".format(location))
        if type == "xpath":
            new_location = self.driver.find_element_by_xpath(location)
        if type == "xpath_text":
            new_location = self.driver.find_element_by_xpath("//*[text()=\"{}\"]".format(location))
        if type == "css_input":
            new_location = self.driver.find_element_by_css_selector("input[placeholder=\"{0}\"]".format(location))
        if type == "css":
            new_location = self.driver.find_element_by_css_selector(location)
        if type == "id":
            new_location = self.driver.find_element_by_id(location)
        new_location.click()
        time.sleep(0.5)



    def list_judgment(self,judge_data,list_position):
        """
        #查询后列表数据判断
        :param judge_data:查询字段judge_data=[name,login_status[1],status[0]]；此列表是已经处理好的，直接使用
        :param list_position:列表字段 list_position=[2,6,9]) ；需要再次定位获取列表的文本信息
        :return:
        """
        actual_result = True
        list_number = int(selenium(self.driver).text_get(location="span.el-pagination__total").split(" ")[1])
        if list_number > 10:
            list_number = 10
        for x in range(list_number):
            text_data = []
            for y in list_position:
                text_data.append(selenium(self.driver).text_get(row=x + 1, column=y))
            if judge_data != text_data:
                actual_result = False
        return actual_result

    def list_data_number(self, location="div.is-scrolling-left>table>tbody", plural=None, location_type="css selector",location_type1="tr"):
        """
        【用此方法】判斷当前定位到的列表表示是否有数据
        :param location: 定位
        :param plural: 复数
        :param location_type: 定位类型
        :param  location_type1：标签名称
        :return: 返回列表数据的条数；支持等于0
        """
        time.sleep(1)
        if plural == None:
            new_location = self.driver.find_element(location_type,location)
        else:
            new_location = self.driver.find_elements(location_type,location)[plural]
        rows = new_location.find_elements_by_tag_name(location_type1)
        before_add_numbers = len(rows)
        return before_add_numbers