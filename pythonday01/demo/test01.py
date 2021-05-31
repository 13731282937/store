from selenium import webdriver

# 创建驱动
driver = webdriver.Chrome()

# 打开网页
driver.get("http://www.baidu.com")

# 窗口最大化
driver.maximize_window()

# 定位搜索框，输入java
driver.find_element_by_id("kw").send_keys("java")

# 点击百度一下
driver.find_element_by_id("su").click()

# 关闭网页
driver.quit()
