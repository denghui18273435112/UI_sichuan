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

@pytest.fixture(scope="session",autouse=True)
def driver():
    """前置：删除report/result的文件信息；登录并返回浏览器驱动；后置：关闭浏览器"""
    #清空报告文件夹下的垃圾文件
    # print("\n>>清空无关图片或文件中....>>\n")
    # try:
    #     for one in os.listdir(result_path):
    #         if "environment.properties" not in one:
    #             os.remove(result_path+os.sep+"{}".format(one))
    #     for one_2 in os.listdir(logs_path):
    #             os.remove(logs_path+os.sep+"{}".format(one_2))
    #     for one_1 in os.listdir(photo_path):
    #         if "_截图" in one_1:
    #             os.remove(photo_path+os.sep+"{}".format(one_1))
    #     if os.path.exists(allure_report_path):
    #         os.rmdir(allure_report_path)
    # except:
    #     print("\n>>没有可删除的文件>>\n")
    # print("\n>>安装最新插件中.....>>\n")
    # os.system("pip freeze > requirements.txt")
    # print("\n>>进入UI自动化测试环节.....>>\n")

    #打开浏览器;输入账号和密码
    option = webdriver.ChromeOptions()
    option.headless =True
    option.add_argument('window-size=1920x1080')
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    while True:
        login =Yaml_read("all_data.yaml","login")
        driver.get(login["url"])
        if selenium(driver).list_data_number("#app > div > div.container > div > div.form > form",location_type1="div") ==12:
            selenium(driver).text_input("请输入账号",login["login_account2"],type="css_1")
            selenium(driver).text_input("请输入密码",login["login_password2"],type="css_1")
            break
        else:
            selenium(driver).resfresh()
    while True:
        #截图验证并设别；直到验证码正常位置
        element =driver.find_element_by_css_selector('form  img')
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        path = _file_path + os.sep + 'code.png'
        driver.save_screenshot(path)
        im = Image.open(path)
        im = im.crop((left, top, right, bottom))
        im.save(path)
        print("\n识别的验证码:{}\n".format(verification_code()))
        selenium(driver).text_input("请输入验证码",verification_code(),type="css_1")
        selenium(driver).click("span.login-button")
        if selenium(driver).get_url() ==login["login_contrast_url"]:
            break
        driver.find_element_by_css_selector('span.login-button').click()
    print("登录成功的cookies信息:{}\n".format(driver.get_cookies()))
    #time.sleep(5)
    yield driver
    driver.quit()