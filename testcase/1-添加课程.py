#@Author: wintone-liwy
#@Description:
#@File:  1-添加课程.py
#@Version: 1.0.0
#@Date: 2020/8/25 10:50
from config.conf import Host,login_url,username,password
from selenium import webdriver
import time

driver =webdriver.Chrome(r"D:\tools\chromedriver\chromedriver.exe")

driver.implicitly_wait(10)
driver.get(login_url)

time.sleep(5)
driver.find_element_by_tag_name("button").click()
time.sleep(2)
# driver.find_element_by_css_selector("body > div > nav > ul > li:nth-child(1) > a").click()
driver.find_element_by_css_selector("ul > li >a").click()
time.sleep(1)
driver.find_element_by_css_selector(".btn.btn-blue.btn-outlined.btn-md").click()
time.sleep(1)
driver.find_element_by_css_selector("div.col-lg-8.col-md-8.col-sm-8 > input:nth-child(1)").send_keys("JAVA开发")
driver.find_element_by_css_selector(" div.col-lg-8.col-md-8.col-sm-8 > textarea").send_keys("大学JAVA开发")
driver.find_element_by_css_selector("div.col-lg-8.col-md-8.col-sm-8 > input:nth-child(3)").clear()
driver.find_element_by_css_selector("div.col-lg-8.col-md-8.col-sm-8 > input:nth-child(3)").send_keys("5")
driver.find_element_by_css_selector(" div.col-lg-12.col-md-12.col-sm-12 > button:nth-child(1)").click()
time.sleep(5)
driver.close()
driver.quit()
