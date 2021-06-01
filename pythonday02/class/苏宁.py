from selenium import webdriver
import time

# 创建编辑器
driver = webdriver.Chrome()

# 打开页面
driver.get(r"https://www.suning.com/")

# 窗口最大化
driver.maximize_window()

# 输入要搜索内容
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电脑")

# 点击搜索
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(3)

# 关闭推荐
driver.find_element_by_xpath("//*[@id='pop418']/a").click()

# 选择电脑
driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_01:0000000000_12157019776']/i/img").click()

# 切换窗口
# 获取所有窗口句柄
wins = driver.window_handles

# 切换操作
driver.switch_to.window(wins[1])

# 选择型号
driver.find_element_by_xpath("//*[@id='colorItemList']/dd/ul/li[3]/a/span").click()
time.sleep(3)

# 点击加入购物车
driver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(3)

# 关闭页面
driver.quit()