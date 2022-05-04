from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

website = "http://www.bredbandskollen.se/"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
time.sleep(5)
driver.find_element_by_xpath('//*[@id="onetrust-button-group"]/div').click()


time.sleep(5)
driver.find_element_by_xpath('//*[@id="mainStartTest"]').click()



time.sleep(25)
text = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div/div/div[2]/span').text
text2 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[2]/span').text
text3 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div/div[3]/div/div/div/div/div[2]/span').text

print(text + '   '+ current_time)
print(text2+ '   '+ current_time)
print(text3+ '   '+ current_time)