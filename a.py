target_hour = 19
target_minute = 14
end_hour = 19
end_minute = 19

import time
import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

def wait_until(hour, minute):
    while True:
        now = datetime.datetime.utcnow()
        if now.hour == hour and now.minute == minute:
            break
        time.sleep(5)

def break_cond():
    now = datetime.datetime.utcnow()
    return now.hour == end_hour and now.minute == end_minute

driver = webdriver.Chrome()
driver.get('https://www.cmlab.csie.ntu.edu.tw/~zeus/src/')
input('please login and click call contract, and then press any key to continue')
print('waiting...')

xpath = '//*[@id="root"]/div/div[3]/button[2]'
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

wait_until(target_hour, target_minute)

while True:
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        button = driver.find_element_by_xpath(xpath)
        button.click()
        print('sent at', datetime.datetime.utcnow())
        time.sleep(1)
    except:
        pass
    if break_cond():
        break
