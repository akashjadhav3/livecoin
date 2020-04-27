# # -*- coding: utf-8 -*-
# import scrapy
# from selenium import webdriver
# from scrapy.selector import Selector
# # from selenium.webdriver.common.keys import Keys # Enter key to submit
# from selenium.webdriver.chrome.options import Options # not open chrome browser
# from shutil import which

# class CoinSpiderSelenium(scrapy.Spider):
#     name = 'coin_selenium'
#     allowed_domains = ['www.livecoin.net/en']
#     start_urls = ['https://www.livecoin.net/en']

#     def __init__(self):
#         chrome_options = Options() # not open chrome browser
#         chrome_options.add_argument("--headless") # not open chrome browser
#         chrome_path = which("./chromedriver")
#         driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options) #options without open chrome browser
#         driver.get("https://www.livecoin.net/en")

#         usa_tab = driver.find_element_by_class_name("filterPanelItem___2z5Gb")
#         usa_tab[3].click()

#         self.html = driver.page_source
#         driver.close()  


#     def parse(self, response):
#         # print(response.body)
#         resp = Selector(text = self.html)
#         for currency in resp.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
#             yield{
#                 'currency_pair':currency.xpath(".//div[1]/div/text()").get(),
#                 'volume(24h)':currency.xpath(".//div[2]/span/text()").get()
#             }




# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en'] 
    start_urls = [
        'https://www.livecoin.net/en'
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("./chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.livecoin.net/en")

        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[2].click()

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }