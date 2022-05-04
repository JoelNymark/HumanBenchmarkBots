from typing import cast
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from time import sleep



website = "https://humanbenchmark.com/tests/aim"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div').click()

driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]').click()

def run():
    try:
        for i in range(30):
            driver.find_element_by_css_selector("div[style='width: 100px; height: 2px;'].css-17nnhwz.e6yfngs4").click()
    finally:
        pass



def checkifdone():
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div[3]/button[1]').click()
            print("DONE")
            return
        except:
            return


run()
checkifdone()