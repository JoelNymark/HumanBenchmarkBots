from typing import Sequence
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from time import sleep


allWebsites =["https://humanbenchmark.com",
                "https://humanbenchmark.com/tests/reactiontime",
                "https://humanbenchmark.com/tests/sequence",
                "https://humanbenchmark.com/tests/aim",
                "https://humanbenchmark.com/tests/number-memory",
                "https://humanbenchmark.com/tests/verbal-memory",
                "https://humanbenchmark.com/tests/chimp",
                "https://humanbenchmark.com/tests/memory",
                "https://humanbenchmark.com/tests/typing"
                ]
website = "https://humanbenchmark.com"
reactoionSite = "https://humanbenchmark.com/tests/reactiontime"
sequenceSite = "https://humanbenchmark.com/tests/sequence"
aimSite = "https://humanbenchmark.com/tests/aim"
numbermemorySite = "https://humanbenchmark.com/tests/number-memory"
verbalSite = "https://humanbenchmark.com/tests/verbal-memory"
chimpsSite = "https://humanbenchmark.com/tests/chimp"
visualSite = "https://humanbenchmark.com/tests/memory"
typeSite = "https://humanbenchmark.com/tests/typing"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

# Press start


def run():
    driver.get(website) 
    time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div').click()

    '''
        log in gunction
    '''
    reactoionTime()
    



def reactoionTime():
    driver.get(reactoionSite) 
    # Press start
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]').click()
    time.sleep(2)


    while True:
        try:
            driver.find_element_by_class_name('view-go').click()
            driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]').click()
        except:
            try:
                driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div[3]/button[1]').click()
            except:
                # print("PASSSSSSS!!!!!!!!")
                pass
        if(driver.current_url == "https://humanbenchmark.com/dashboard"):
            sequence()


def sequence():
    print("Start Sequence!!!!!!!!!!!!!!!!")
    driver.get(sequenceSite) 
    # Press start
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]').click()
    time.sleep(2)

    tiles = driver.find_elements_by_css_selector("div.square")
    print("TILES PRINT OUT : "+ str(tiles))
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
    fail() ## change to next level i think!

    return level

def fail():
    try:  # Click until element is no longer available to click
        while True:
            time.sleep(0.1)
            driver.find_element_by_css_selector("div.square").click()
    except:
        pass


def checkifdone():
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div[3]/button[1]').click()
            print("DONE")
            return
        except:
            return

def runNextChalange():
    for i in range(len(allWebsites)):
        curentwebpage = allWebsites[i]
        

runNextChalange()