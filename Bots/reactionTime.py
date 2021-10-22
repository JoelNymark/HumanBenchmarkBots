from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

website = "https://humanbenchmark.com/tests/reactiontime"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/button').click()

while True:
    try:
        time.sleep(.001)
        driver.find_element_by_class_name('view-go').click()
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]').click()
    except:
        pass





# //*[@id="root"]/div/div[4]/div[1]