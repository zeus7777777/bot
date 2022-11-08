import datetime
import json
import requests
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

block_base = 3368160
block_offset = 1440

offset = -2
duration = 5

def get_current_height():
    try:
        r = requests.get('https://nodes.wavesnodes.com/blocks/last')
        current_height = int(json.loads(r.text)['height'])
        return current_height
    except:
        return 0

def wait_until(height):
    print('waiting...')
    last = 0
    while True:
        current = get_current_height()
        if current != last:
            print(current)
            last = current
        if  current >= height:
            break
        else:
            time.sleep(15)

current_height = get_current_height()
target_height = block_base + block_offset * ((current_height - block_base) // block_offset + 1) + offset
print('current_height', current_height)
print('target_height', target_height)

driver = webdriver.Chrome()
driver.get('https://www.cmlab.csie.ntu.edu.tw/~zeus/src/')
input('please login and click call contract, and then press any key to continue')

xpath = '//*[@id="root"]/div/div[3]/button[2]'
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

wait_until(target_height)

while True:
    try:
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        button = driver.find_element(By.XPATH, xpath)
        button.click()
        print('sent at', datetime.datetime.utcnow())
    except:
        pass
    if get_current_height() >= target_height + duration:
        break
