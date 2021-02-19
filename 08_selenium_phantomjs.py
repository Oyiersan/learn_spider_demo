
# https://mp.weixin.qq.com/s/pGyFYpAoMtgGtD4uxBSCig

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import xlwt

from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Chrome()
browser.get("https://www.bilibili.com/")

# 就是等到这个元素可操作的时候才会继续执行下一步
# WAIT.until
WAIT = WebDriverWait(browser, 10)


def get_source():
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#all-list > div.flow-loader > div.filter-wrap')))
    # all-list > div.flow-loader > div.mixin-list > ul
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    print('到这')
    list = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')
    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biubiu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text
        print('爬取打篮球：' + item_title + ' | ' + item_link + ' | ' + item_dec + ' | ' + item_view + '|' + item_biubiu + '|' + item_date)

    pass

# 输入框
# //*[@id="nav_searchform"]/input
# #nav_searchform > input
# input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner_link > div > div > form > input")))
input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav_searchform > input")))
# 搜索框
# #nav_searchform > div > button
# submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))
# //*[@id="nav_searchform"]/div/button
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav_searchform"]/div/button')))

input.send_keys('蔡徐坤 篮球')
submit.click()

 # 去除弹出的登录提示框
# index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#primary_menu > ul > li.home > a")))
# index.click()

# 跳转到新的窗口
print('跳转到新窗口')
all_h = browser.window_handles
browser.switch_to.window(all_h[1])

total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                           "#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.last > button")))
total_num = int(total.text)
print('总页数' + total_num)

get_source()



