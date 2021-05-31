from selenium import webdriver
import time

'''
在百度中搜索Java
'''

# 创建驱动
dricer = webdriver.Chrome()

# 打开网页
dricer.get("http://www.baidu.com")

#窗口最大化
dricer.maximize_window()

# 定位输入框，并输入Java
dricer.find_element_by_id("kw").send_keys("java")

#点击百度一下
dricer.find_element_by_id("su").click()

time.sleep(4)

# 关闭页面
dricer.quit()
