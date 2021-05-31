from selenium import webdriver
import  time

# 创建驱动
driver = webdriver.Chrome()

# 打开网页
driver.get(r"D:\python自动化测试技术\python代码class\python自动化\day01\资料\练习的html\练习的html\弹框的验证\dialogs.html")
time.sleep(2)

# 点击alert按钮
driver.find_element_by_id("alert").click()
# 点击确定
driver.switch_to.alert.accept()
time.sleep(2)

# 点击confirm按钮
driver.find_element_by_id("confirm").click()
# 点击取消
driver.switch_to.alert.dismiss()



time.sleep(3)

#关闭页面
driver.quit()