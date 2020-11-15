"""
Group4 - Price Comparisons
"Search for retail product API"
"Implement API into program"
"Write code that calculates price differences"
"Create input for users products"
"""
import sys
from selenium import webdriver


class walmart_scraper(object): 
    def __init__(self,query,max_price):
        self.browser = webdriver.Chrome
        self.max_price = max_price
        self.query = query
        self.url = f"https://www.walmart.com/search/?max_price=1000&min_price=&page=1&query=TV&value=till+%243000"
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.delay = 5
    
    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements_by_class_name("Grid-col u-size-6-12 u-size-1-4-m u-size-1-5-xl search-gridview-first-grid-row-item")
        for data in all_data:
            print(data.text)

query = "TV"
max_price = 1000
scraperws = walmart_scraper(query,max_price)
scraperws.load_page()


class target_scraper(object):
    def __init__(self,searchTerm,maxPrice):
        self.maxPrice = maxPrice
        self.searchTerm = searchTerm
        self.url = f"https://www.target.com/s?searchTerm=tv&minPrice=0&maxPrice=1000&Nao=0"
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.delay = 5
        
    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements_by_class_name("react-rendered")
        for data in all_data:
            print(data.text)
        
searchTerm = "tv"
maxPrice = 1000
scrapert = target_scraper(searchTerm,maxPrice)
scrapert.load_page()