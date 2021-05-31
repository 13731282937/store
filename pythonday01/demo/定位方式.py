from selenium import webdriver
import time

# 创建驱动
driver = webdriver.Chrome()

# 打开网页
driver.get(r"D:\python自动化测试技术\python代码class\python自动化\day01\资料\练习的html\练习的html\main.html")

# 窗口最大化
driver.maximize_window()

# 定位frame页面
driver.switch_to.frame("frame")

# 根据id定位，并输入值
driver.find_element_by_id("input1").send_keys("123456")

time.sleep(4)

# 关闭页面
driver.quit()



