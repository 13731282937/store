from selenium import webdriver
import time

#创建编辑器
driver = webdriver.Chrome()

# 打开网页
driver.get(r"D:\python自动化测试技术\python代码class\python自动化\html\练习的html\上传文件和下拉列表\autotest.html")

# 输入用户名（输入框输入内容）
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("杰克马")
time.sleep(2)

# 清空输入名（清空输入框）
driver.find_element_by_xpath("//*[@id='accountID']").clear()
time.sleep(2)

# 输入性别（按钮点击）
driver.find_element_by_xpath("//*[@id='sexID1']").click()

# 输入地区(下拉选项)
driver.find_element_by_css_selector("[value='beijing']").click()
time.sleep(2)

# 上传文件(上传文件)
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"D:\python自动化测试技术\classtest\da.xlsx")
time.sleep(3)



# 关闭页面
driver.quit()