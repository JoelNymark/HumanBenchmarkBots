from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

website = "https://humanbenchmark.com/tests/memory"

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver', options = chrome_options)

driver.get(website) 
# Press start
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]').click()

tile_selector = "div.square"

def run():
    # Level loop
    # Add max since it's unable to read all squares to click around level 118
    for level in range(1, 100 + 1):
        time.sleep(0.5)  # Wait half a second for squares to light up
        squares = driver.find_elements_by_css_selector("div.css-lxtdud")

        indicator = None
        for i, square in enumerate(squares):
            if "active" not in square.get_attribute("class"):
                squares[i] = None
                print("1")

            elif indicator is None:
                indicator = square
                print("2")

        while "active" in square.get_attribute("class"):
            time.sleep(0.1)
        time.sleep(0.5)  # Extra wait to prevent element not interactable error

        for square in filter(None, squares):
            time.sleep(.6)
            square.click()
            print("3")
run()




# def run():

#     tiles = driver.find_elements_by_css_selector("div.css-lxtdud")
#     curLevel = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]/span[1]/span[2]').text
#     sequence = []


#     nextLevel = int(curLevel) + 1

#     print("This is level : " + str(curLevel))
#     print("Next Level is : " + str(nextLevel))

    
    # print(len(tiles))  
    # while True:
    #     time.sleep(.5)
    #     for tile in tiles:
    #         #try:
    #         # print("tile class attributes : " + str(tile.get_attribute("class")))
    #         IsActive =  "active" in tile.get_attribute("class")
    #         if(IsActive):
    #             sequence.append(tile)
    #             print("ADDED TO LIST")
        
        
        
        
        # for i in range(len(sequence)):
        #     try:
        #         # print("is sequence is as long as level : " + str(len(sequence) != len(curLevel)))
        #             # print(sequence)
        #             sequence[i].click()
        #             print("Button : " + str(sequence[i]) + "was pressed !!!-----------------------------------")
        #     except:
        #         print("Reseting sequence")
        #         sequence = []
        #         tiles = []
        #         print("tiles list : " + str(tiles))
    





        # for tile in tiles:
        #     #try:
        #     print("tile class attributes : " + str(tile.get_attribute("class")))
        #     IsActive =  "active" in tile.get_attribute("class")
        #     if(IsActive):
        #         sequence.append(tile)
        #         print("ADDED TO LIST")
        #     if (len(sequence) == (int(level) + 1)):
        #         print(len(sequence) == len(curLevel))
        #         for i in range(len(sequence)):
        #             print(sequence)
        #             sequence[i].click()
        #     else:
        #         resetSeq = True

        #     if(resetSeq == True):
        #         sequence = []
        #         print("secuwns is empty now  : " + str(sequence))
        #         resetSeq = False





            # except:
        #     print("asdasdasds")     
        #     time.sleep(2)   
        #     for i in sequence:
        #         time.sleep(0.1)
        #         tiles[i].click()