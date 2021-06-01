from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# 创建编辑器
driver = webdriver.Chrome()

# 打开页面
driver.get(r"https://www.jd.com/")

# 窗口最大化
driver.maximize_window()

# 登录(扫码登录)
driver.find_element_by_link_text("你好，请登录").click()
time.sleep(20)

# 搜索商品
driver.find_element_by_xpath("//*[@id='key']").send_keys("电脑")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(3)

# 点击商品
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div/div[1]/a/img").click()
time.sleep(3)

# 切换窗口
# 获取所有窗口句柄
wins = driver.window_handles

# 切换操作
driver.switch_to.window(wins[1])

# 选择型号
driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[1]/a/i").click()
time.sleep(2)

# 加入购物车
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(3)

# 关闭页面
driver.quit()