from selenium import webdriver
from tools.Yaml_read import Yaml_read

option = webdriver.ChromeOptions()
option.headless =False
option.add_argument('window-size=1920x1080')
option.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=option)
driver.maximize_window()
login =Yaml_read("all_data.yaml","login")
driver.get(login["url"])
driver.implicitly_wait(100)
dd = driver.find_element_by_css_selector("input[placeholder='请输入账dadsa号']")
dd.send_keys(login["login_account1"])
