from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

website = "https://humanbenchmark.com/tests/sequence"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]').click()
seqList = []
seqLoop = True
clickLoop = False

# while True:
#     while seqLoop:
#         if(len(seqList) != int(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]/span/span[2]').text)):
            
#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[1]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[1]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[2]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[2]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[3]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[3]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[2]/div[1]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[2]/div[1]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[2]/div[2]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[2]/div[2]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[2]/div[3]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[2]/div[3]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[3]/div[1]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[3]/div[1]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[1]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[3]/div[2]'))

#             if(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div[1]').get_attribute('class') == 'square active'):
#                 time.sleep(.1)
#                 seqList.append(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div/div[3]/div[3]'))
          
#             time.sleep(.3)
#             print(seqList)
#         else:
#             clickLoop = True
#             seqLoop = False
#             print("seqloop end")

#     time.sleep(1)
#     while clickLoop:
#         for x in seqList:
#             x.click()
#             print(x)
#         seqList = []
#         seqLoop = True
#         time.sleep(.5)
#         clickLoop = False
#         print("clickloop end")

def run():

    tiles = driver.find_elements_by_css_selector("div.square")

    for level in range(1, 50 + 1):
        sequence = []
        time.sleep(0.5)
        while len(sequence) < level:
            active = None
            for i, tile in enumerate(tiles):
                if "active" in tile.get_attribute("class"):
                    sequence.append(i)
                    active = tile
                    break

            while active and "active" in active.get_attribute("class"):
                time.sleep(0.1)

        for i in sequence:
            time.sleep(0.1)
            tiles[i].click()
    fail()

    return level

def fail():
    try:  # Click until element is no longer available to click
        while True:
            time.sleep(0.1)
            driver.find_element_by_css_selector("div.square").click()
    except:
        pass

run()