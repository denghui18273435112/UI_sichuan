#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : jss.py
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
url = 'http://www.cnblogs.com/sanzangTst/'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
time.sleep(3)
# 拉到底部
#js="var q=document.documentElement.scrollTop=10000"
#js="var q=document.getElementsByClassName('skin-codinglife').scrollTop=0"
js="var q=document.getElementById('id').scrollTop=10000"
browser.execute_script(js)
time.sleep(3)
# 回到顶部
#js="var q=document.documentElement.scrollTop=0"

js="var q=document.getElementById('id').scrollTop=0"
browser.execute_script(js)
time.sleep(3)
# 拖到指定位置
# target = browser.find_element_by_id("homepage1_HomePageDays_DaysList_ctl05_DayList_TitleUrl_0")
# browser.execute_script("arguments[0].scrollIntoView();", target)

#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
browser.execute_script(js)
time.sleep(3)
#滚动到顶部
js = "window.scrollTo(0,0)"
browser.execute_script(js)
time.sleep(3)