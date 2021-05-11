import os
import random
import time
import urllib.request

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.health.kr/searchIdentity/search.asp'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(URL)

driver.implicitly_wait(time_to_wait=5)

type_bt = driver.find_element_by_id('type_all')

shape_bt_1 = driver.find_element_by_xpath('//*[@id="shape_01"]/a/img')
shape_bt_2 = driver.find_element_by_xpath('//*[@id="shape_02"]/a/img')
shape_bt_3 = driver.find_element_by_xpath('//*[@id="shape_03"]/a/img')
shape_bt_4 = driver.find_element_by_xpath('//*[@id="shape_04"]/a/img')
shape_bt_5 = driver.find_element_by_xpath('//*[@id="shape_05"]/a/img')
shape_bt_6 = driver.find_element_by_xpath('//*[@id="shape_06"]/a/img')
shape_bt_7 = driver.find_element_by_xpath('//*[@id="shape_07"]/a/img')
shape_bt_8 = driver.find_element_by_xpath('//*[@id="shape_08"]/a/img')
shape_bt_9 = driver.find_element_by_xpath('//*[@id="shape_09"]/a/img')
shape_bt_10 = driver.find_element_by_xpath('//*[@id="shape_10"]/a/img')

color_bt = driver.find_element_by_xpath('//*[@id="color_all"]/a')

line_bt_no = driver.find_element_by_xpath('//*[@id="line_no"]/a')
line_bt_plus = driver.find_element_by_xpath('//*[@id="line_plus"]/a')
line_bt_minus = driver.find_element_by_xpath('//*[@id="line_minus"]/a')

search_bt = driver.find_element_by_xpath('//*[@id="btn_idfysearch"]')

# search_bt.click()

def page_move(driver):
    page_bar = driver.find_element_by_css_selector('#paging')
    pages = page_bar.find_elements_by_css_selector('a')
    page_now = page_bar.find_element_by_class_name('current').text
    page_list = []

    for page in pages:
        page_list.append(page.text)
    page_list.remove('')
    page_list.remove('')
    page_list.remove('')
    page_list.remove('')
    print(page_list)

    for page in pages:
        if page.text == '':
            continue
        page_num = page.text
        print(page_num, page_now)
        if int(page_num) == int(page_now):
            nextpage = page.find_element_by_xpath("//a[text() = '{}']".format(int(page_num) + 1))
            nextpage.click()
            return page_num, False
        if page_num == page_list[-1]:
            print('마지막페이지')
            return page_num, True


for i in range(1, 3):
    eval('shape_bt_' + str(i)).click()
    search_bt.click()

    if not os.path.isdir('./{}'.format('shape_bt' + str(i))):
        os.mkdir('./{}'.format('shape_bt' + str(i)))

    chk = False
    while (not chk):
        page_num, chk = page_move(driver)

        for j in range(3, 53):
            img = driver.find_element_by_xpath('//*[@id="idfytotal0"]/tbody/tr[{0}]/td[1]/div/a/img'.format(j))
            src = img.get_attribute('src')
            urllib.request.urlretrieve(src, './shape_bt{0}/{1}_{2}.png'.format(i, page_num, j))
