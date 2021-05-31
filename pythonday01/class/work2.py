'''
框架页的切换
'''

from selenium import webdriver
import time

# 创建驱动
driver = webdriver.Chrome()

# 打开页面
driver.get(r"file:///D:/python%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E6%8A%80%E6%9C%AF/python%E4%BB%A3%E7%A0%81class/python%E8%87%AA%E5%8A%A8%E5%8C%96/day01/%E8%B5%84%E6%96%99/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E7%BB%83%E4%B9%A0%E7%9A%84html/main.html")
time.sleep(2)

# 定位frame
driver.switch_to.frame("frame")

# 输入框输入内容
driver.find_element_by_xpath("//*[@id='input1']").send_keys("123456")
time.sleep(3)

# 关闭页面
driver.quit()