hh = 3
mm = 15
duration = 6

import time
import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.cmlab.csie.ntu.edu.tw/~zeus/src/')
input('please login and click call contract, and then press any key to continue')
print('waiting...')

xpath = '//*[@id="root"]/div/div[3]/button[2]'
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

while True:
    if datetime.datetime.now().hour == hh and datetime.datetime.now().minute == mm:
        break
    time.sleep(5)
while True:
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        button = driver.find_element_by_xpath(xpath)
        button.click()
        print('sent at', datetime.datetime.now())
        time.sleep(1)
    except:
        pass
    if datetime.datetime.now().minute > mm + duration:
        break
