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