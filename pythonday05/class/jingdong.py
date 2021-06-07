# encoding=utf-8

from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',          # 需替换成你的driverName
    'platformVersion': '7.1.2',
    'appPackage': 'com.jingdong.app.mall',
    'appActivity': 'com.jingdong.app.mall.main.MainActivity'
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
driver.find_element_by_id("com.jingdong.app.mall:id/bqd").click()
time.sleep(20)

driver.find_element_by_class_name("android.widget.ViewFlipper").click()
time.sleep(3)
driver.find_element_by_id("com.jd.lib.search.feature:id/zw").send_keys("手机")
time.sleep(1)
driver.find_element_by_id("com.jingdong.app.mall:id/a9b").click()
time.sleep(1)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]").click()
time.sleep(1)
driver.find_element_by_id("com.jd.lib.productdetail.feature:id/pd_invite_friend").click()
time.sleep(1)
driver.tap([(457,1552)],50)

driver.quit()







