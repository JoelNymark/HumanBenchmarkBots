from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

website = "https://humanbenchmark.com/tests/typing"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/button').click()
time.sleep(.5)

while True:
    letter = driver.find_element_by_class_name('current').text
    
    if(letter == ""):
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div').send_keys(Keys.SPACE)
    else:    
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div').send_keys(str(letter))
