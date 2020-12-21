'''
Names: Kyo Lee, Mahad Abdi, Lucas Gordon, Kyle Breitenother
Date: 12/20/2020
Assignment: Final Project
'''
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class target_crawler(object):
    """
    A class to represent the crawler bot for Target website.
    
    Attributes
    ----------
    url : str
        the url address of the website.
    driver: 
        using Google chrome to open the url.
    user_input : str
        number of pages to scrape for the website.

    Methods
    -------
    crawler(url, driver, prd_names, brand_names, sale_prices, reg_prices, user_input, num_page=0, count=0):
        scrapes data from the Target website.
    """
    def __init__(self):
        """
        Constructs the necessary attributes to initialize the crawler.

        Parameters
        ----------
        url : str
            the url address of the website.
        driver: 
            using Google chrome to open the url.
        user_input : str
            number of pages to scrape for the website.
        """
        self.url = f'https://www.target.com/c/tvs-home-theater-electronics/-/N-5xtdj?Nao=0'
        self.driver = webdriver.Chrome("chromedriver.exe")
        
        # target tv has 3 pages (for future, may make it so it finds the pages length)
        self.user_input = input('Number of pages to scrape target: ')
        
    def crawler(self, num_page=0):
        """
        Scrapes the necessary data of the items from the website and converts into csv file.
        All the data that are scrape from the website are appended to the corresponding lists.

        Parameters
        ----------
        num_page: int (default=0)
            page index for url address to search for the items in the next page.
        
        Arguments
        ----------
        url : str
            the url address of the website.
        driver: 
            using Google chrome to open the url.
        prd_names: str, list
            list of product names.
        brand_names: str, list
            list of brand names.
        sale_prices: int, list
            list of product sale prices that are converted to integers when appending to the list.
        reg_prices: int, list
            list of product regular prices that are converted to integers when appending to the list.
        user_input : str
            number of pages to scrape for the website.

        Raises
        -------
        NoSuchElementException : sets the price value to '0' if no price value is found.
        
        Side effects
        -------
        Appends product names to the prd_names list.
        Appends brand names to the brand_names list.
        Appends sale prices to the sale_prices list.
        Appends regular prices to the reg_prices list.
        Creates csv file by using pandas to get dataframe of the prd_names, brand_names, sale_prices, and reg_prices
        """
        url = self.url
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(url)
        
        prd_names = []
        brand_names = []
        sale_prices = []
        reg_prices = []
        
        user_input = self.user_input

        last = int(user_input) * 24 - 1
        # opens url and next pages
        while num_page < last + 1:
            url = f'https://www.target.com/c/tvs-home-theater-electronics/-/N-5xtdj?Nao={num_page}'
            driver.implicitly_wait(10)
            driver.get(url)
            
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

            # product names and brand names
            elems = driver.find_elements_by_css_selector(".styles__PriceInfoTile-sc-1ip0qfy-1.hqUeIt.h-text-left.h-margin-v-tight [href]")
            names = [elem.get_attribute('innerHTML') for elem in elems]
            
            for e in names:
                if e == 'Check nearby stores':
                    names.remove(e)
                elif e == 'See Similar Items':
                    names.remove(e)
                else:
                    continue
            
            n = 0
            for i in names: 
                if (n % 2 == 0): 
                    prd_names.append(i)
                    n+=1
                else:
                    brand_names.append(i)
                    n+=1
                    
            # finds the links for each tvs
            links = driver.find_elements_by_css_selector(".Col-favj32-0.jMuXHi [href]")
            prd_links = [elem.get_attribute('href') for elem in links]
        
            # opens each tv links
            for a in prd_links:
                url = f'{a}'
                time.sleep(.5)
                driver.get(url)
            
                # product sale prices and regular prices
                prices_s = driver.find_element_by_css_selector("#viewport div.style__PriceFontSize-sc-17wlxvr-0.cYCpyy").text
                try:
                    prices_r = driver.find_element_by_css_selector("#viewport span.h-margin-v-tight.h-text-sm.h-text-grayDark").text[4:11]
                except NoSuchElementException:
                    prices_r = '0'
                    
                sale_prices.append(int(prices_s.replace('$', '').replace('.', '').replace(',', '')))
                reg_prices.append(int(prices_r.replace('$', '').replace('.', '').replace(',', '')))
            
            num_page += 24
            count += 1
        
        driver.close() 
        
        df = pd.DataFrame({'Product Names': prd_names, 'Brand Names': brand_names, 'Regular Price: ': reg_prices, 'Sale Price: ': sale_prices})
        name = df.values.tolist()
        df.to_csv('target_tv_dataset.csv') 
        print(name)
        
    
        

class bestbuy_crawler(object):
    '''Class that web scrapes best buy tv bestsellers for their type and price. Creates a csv file with that data.
    
    Attributes:
        url (str): The base url for the bestsellers list.
        driver (WebDriver): the driver tool used to scrape the site.
        w (str): the user input for how many pages to scrape.
    '''
    
    def __init__(self):
        self.url = f'https://www.bestbuy.com/site/promo/tv-deals?cp=1&qp=category_facet%3DTVs~abcat0101000&sp=-bestsellingsort%20skuidsaas'
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.w = input("Number of pages to scrape bestbuy: ")
    
    def crawler(self):
        '''Crawls best buy tv product pages and appends the realitive price and type data to its list. Creates a csv file from a dataframe containing price and type information.
        
        Raises:
            NoSuchElementException : if the price or type can't be found it gives a deafault.
        
        Side effects:
            Appends TV prices to tv_price list
            Appens TV types to tv_type list
            Creates csv file from the data frame of the tv prices and types
            
        '''
        
        url = self.url
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(url)
        
        tv_type = []
        tv_price = []
        
        w = self.w
        num_page = 0
        count = 1
        last = int(w) *24 - 1
        while num_page < last + 1:
            url = f"https://www.bestbuy.com/site/promo/tv-deals?cp={num_page}&qp=category_facet%3DTVs~abcat0101000&sp=-bestsellingsort%20skuidsaas"
            driver.implicitly_wait(10)
            driver.get(url)

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

            links = driver.find_elements_by_css_selector(".image-column [href]")
            prd_links = [elem.get_attribute('href') for elem in links]
            
            for a in prd_links:
                url = f'{a}'
                time.sleep(.5)
                driver.get(url)
                
                try:
                    tv_name = driver.find_element_by_xpath(xpath="//div[contains(concat(' ', @class, ' '), ' sku-title ')]//h1[1]").text
                    
                
                except NoSuchElementException:
                    tv_name = 'TV Unknown'
                tv_type.append(str(tv_name))
                
                
                
                try:
                    prices_w = driver.find_element_by_xpath(xpath="//div[contains(concat(' ', @class, ' '), ' priceView-hero-price priceView-customer-price ')]//span[1]").text
                    
                except NoSuchElementException:
                    prices_w = '0' 
                tv_price.append(int(prices_w.replace('$', '').replace('.', '').replace(',', '')))
            num_page += 24
            count += 1
        driver.close()
    
        wdf = pd.DataFrame({'TV Name': tv_type, 'TV Price: ': tv_price})
        name = wdf.values.tolist()
        wdf.to_csv('bestbuy_tv_dataset.csv')
        print(name)
        
        
if __name__ == "__main__":               
    crawler = target_crawler()
    crawler2 = bestbuy_crawler()
    crawler.crawler()
    crawler2.crawler()
    
