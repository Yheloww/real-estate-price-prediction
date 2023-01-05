<<<<<<< HEAD
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from csv import writer
import re
import json

# https://www.immoweb.be/en/search/house-and-apartment/for-sale/brussels/province?countries=BE&page=1&orderBy=relevance

# provinces list
provinces_list=["antwerp", "brabant", "brussels", "west-flanders", "east-flanders", "hainaut", "liege", "limburg", "luxembourg", "namur"]
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
=======
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import time
from csv import writer

# currently not working at some points

# json creation
doc = f"./test.json"

# webdriver setup
def driversetting():
    driver = webdriver.Firefox()
    return driver

# scraping
def scraping(iteration, driver):
    list_of_properties = []
    provinces = ["antwerp", "brabant", "brussels", "west-flanders", "east-flanders", "hainaut", "liege", "limburg", "luxembourg", "namur"]

    for prov in range(len(provinces)):
        province=provinces[prov]
        for number in iteration:
            page_num = str(number)
            url = ("https://www.immoweb.be/en/search/house-and-apartment/for-sale/"+province+"/pronvince?countries=BE&page="+page_num+"&orderBy=relevance")

            driver.get(url)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            listings = soup.find_all("a", class_="card__title-link")
            for pages in listings:  
                driver.get(pages["href"]) # get the response from the url
                property_details_page = BeautifulSoup(driver.page_source, "html.parser")
                content = property_details_page.find("section", class_="classified_section")
                list_of_properties.append(content)
        return list_of_properties

# json writing
def saving_datas(datas):
    with open(doc, 'a') as file:
        json.dump(str(datas), file, indent=4)

# concurrency setting
def pool():
    # 1 driver by thread (we have four thread here)
    drivers = [driversetting() for _ in range(8)]
    #division of the number of pages by the number of threads 
    division = np.array_split(np.arange(1,8),8)
    #creation of a pool of threads
    with ThreadPoolExecutor(max_workers=8) as executor :
        results = executor.map(scraping,division,drivers)
        for result in results: 
            saving_datas(result)

pool()
>>>>>>> 6aba6fb (trying to incorporate Heloise functions)
