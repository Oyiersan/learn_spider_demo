# https://mp.weixin.qq.com/s/pNs5VBLadYQbe8RjsR4x1g
# https://selenium-python.readthedocs.io/

from selenium import webdriver

# 获取浏览器对象实例
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

input = driver.find_element_by_css_selector('#kw')
input.send_keys("苍老师照片")

button = driver.find_element_by_css_selector('#su')
button.click()