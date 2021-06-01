from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# 创建编辑器
driver = webdriver.Chrome()

# 打开网页
driver.get(r"https://www.qcc.com/")

# 最大化窗口
driver.maximize_window()
time.sleep(3)

# 关闭推荐页
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]/img[1]").click()


# 点击登录
driver.find_element_by_link_text("登录 | 注册").click()
time.sleep(3)

# 获取滑块
ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

# 创建actionchains
ac = ActionChains(driver)

# 滑动滑块
ac.click_and_hold(ele).move_by_offset(347.99,0).perform()
time.sleep(3)

# 关闭页面
driver.quit()