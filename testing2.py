"""
"Search for retail product API"
"Implement API into program"
"Write code that calculates price differences"
"Create input for users products"
"""
import re
import time
from selenium import webdriver

class target_crawler(object):
    def __init__(self):
        self.url = f"https://www.target.com/c/tvs-home-theater-electronics/-/N-5xtdj?Nao=0"
        self.driver = webdriver.Chrome("chromedriver.exe")
        
    def get_links(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get(self.url)
        
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(.5)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        links = driver.find_elements_by_css_selector(".Col-favj32-0.jMuXHi [href]")
        all_links = [elem.get_attribute('href') for elem in links]
        
        print(len(all_links))
        
crawler = target_crawler()
crawler.get_links()