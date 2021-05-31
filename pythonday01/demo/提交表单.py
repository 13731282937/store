from selenium import webdriver
import time

# 获取驱动
driver = webdriver.Chrome()

# 打开页面
driver.get(r"D:\python自动化测试技术\python代码class\python自动化\day01\资料\练习的html\练习的html\上传文件和下拉列表\autotest.html")

# 输入用户名
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("杰克马")

# 输入密码
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")

# 输入地区
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京")

# 输入性别
driver.find_element_by_xpath("//*[@id='sexID1']").click()

# 输入四季
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='winter']").click()

# 上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"D:\python自动化测试技术\classtest\da.xlsx")

time.sleep(3)

# 关闭页面
driver.quit()