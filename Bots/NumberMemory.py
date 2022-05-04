from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

website = "https://humanbenchmark.com/tests/number-memory"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/button').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]').click()

words = []



def Number():
    number = driver.find_element_by_class_name("big-number ").text
    while True:
        try:
            numberInput = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input')
            numberInput.send_keys(str(number))
            numberInput.send_keys(Keys.RETURN)
            driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()
            Number()
        except:
            pass

Number()


