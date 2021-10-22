from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

website = "https://humanbenchmark.com/tests/verbal-memory"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/button').click()

words = []

def CheckWord():

    word = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div').text
    isInList = False
    for x in words:
        if(word == x):
            isInList = True
        
    if(isInList == False):
        words.append(word)
        # press new word button
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()
        # print(word)
        CheckWord()
        
    else:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()
        CheckWord()

CheckWord()
