"""
Scraping price data from retailers and comparing.
"""
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

class Retail():
    def targetprice():
        baseUrl = "https://www.target.com/"
        plusUrl = input('Choose your category to shop:')
        url = baseUrl + "s?searchTerm=" + quote_plus(plusUrl)

        driver = webdriver.Chrome("chromedriver.exe")
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html)

        link = soup.select('.h-display-flex')
        print(type(link))
        for i in link:
            print(i.select_one('.product-title'))
            print(i.select_one('href'))
            
            #<class 'bs4.element.ResultSet'>
            
        driver.close

    def walmartprice():
        wPrices=[]


        page = requests.get("http://www.walmart.com/search/?max_price=1000&min_price=&page=1&query=TV&value=till+%243000")
        soup = BeautifulSoup(page.text, "html.parser")
        walmart = soup.findAll('section', href=True, attrs={'class':'section.search-app.search-desktop-app.feature-ny.feature-2dayshipping.feature-2price-1.feature-2price-2.no-skyline'})

        i = 0 
        while i < 200:
            url = "http://www.walmart.com/search/?max_price=1000&min_price=&page=1&query=TV&value=till+%243000" + walmart[i]["class"]
            price=i.find('span', attrs={'class':'price-characteristic'})
            wPrices.append(price.text)

        df = pd.DataFrame({'Price':wPrices})