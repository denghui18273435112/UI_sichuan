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

#打开浏览器;输入账号和密码
option = webdriver.ChromeOptions()
option.headless =False
option.add_argument('window-size=1920x1080')
option.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=option)
driver.maximize_window()

driver.get("https://www.baidu.com/")
driver.implicitly_wait(50)
search_jq = "$('//*[@id='kw']').val('selenium')"
button_jq = "$('.s_btn').click()"
driver.execute_script(search_jq)
driver.execute_script(button_jq)
time.sleep(10)
driver.quit()