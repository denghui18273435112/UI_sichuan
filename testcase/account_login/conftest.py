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
    print("\n>>清空无关图片或文件中....>>\n")
    try:
        pass
    except:
        print("\n>>没有可删除的文件>>\n")
    print("\n>>安装最新插件中.....>>\n")
    os.system("pip freeze > requirements.txt")
    print("\n>>进入UI自动化测试环节.....>>\n")

    #打开浏览器
    option = webdriver.ChromeOptions()
    option.headless =True
    option.add_argument('window-size=1920x1080')
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    yield driver
    driver.quit()