from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from csv import writer
import re
import json

# https://www.immoweb.be/en/search/house-and-apartment/for-sale/brussels/province?countries=BE&page=1&orderBy=relevance

# provinces list
provinces_list=["antwerp", "brabant", "brussels", "west flanders", "east flanders", "hainaut", "liege", "limburg", "luxembourg", "namur"]
for y in range(len(provinces_list)):
    province=provinces_list[y]
    # page number
    for i in range(1, 2):
        page_num = str(i) + "&orderBy=relevance"
        url = (
            "https://www.immoweb.be/en/search/house-and-apartment/for-sale/"+province+"/province?countries=BE&page="+page_num
        )
        list_of_properties = []

        driver = webdriver.Firefox()
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        listings = soup.find_all("a", class_="card__title-link")

        for pages in listings:  

            property_details = {}
            driver.get(pages["href"]) 
            property_details_page = BeautifulSoup(driver.page_source, "html.parser")

            script_list = property_details_page.find_all("script")
            print(script_list)
    #       readable = re.sub(r'[\\/]', '', script_list)
    #       print(readable)


# Let's make it work
'''
        for list in pages:

            title = list.find('a', attrs={"class":"cardtitle-link"})
            locality = list.find('p', attr={"class":"cardinformation card--resultsinformation--locality cardinformation--locality"})
            typeproperty = list.find('a', attr={"class":"cardtitle-link"}).text
            price = list.find('span', attr={"class":"sr-only"})

            info = [title, locality, typeproperty, price]
            print(info)
'''