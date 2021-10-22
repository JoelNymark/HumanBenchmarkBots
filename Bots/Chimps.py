from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

website = "https://humanbenchmark.com/tests/chimp"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/button').click()

def Buttons():
    allbuttons = driver.find_elements_by_class_name('css-19b5rdt')

    for i in range(len(allbuttons)):
        try:
            for button in allbuttons:
                try:
                    if(button.get_attribute("data-cellnumber") == str(i+1)):
                        button.click()
                except:
                    print("no")
                    driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[3]').click()
                    Buttons()
        except:
            print("nonono")
            Buttons()
Buttons()
