from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import pandas as pd
from threading import Thread
#import for threading
from concurrent.futures import ThreadPoolExecutor
from threading import RLock
import time
import numpy as np

#
test = f"./datasss.json"

def driversetting():
    #need to set up the driver outside of the scraping part bc we need several drivers
    driver = webdriver.Chrome(executable_path="driver/chromedriver")

    return driver

def scraping(iteration, driver):
    list_of_properties = []

    for number in iteration:
        page_num = str(number) + "&orderBy=relevance"
        url = (
            "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page=" + page_num
        )

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        listings = soup.find_all("a", class_="card__title-link")
        for pages in listings:  

            driver.get(pages["href"]) # get the response from the url
            property_details_page = BeautifulSoup(driver.page_source, "html.parser")
            content = property_details_page.find("section", class_="classified_section")
            list_of_properties.append(content)
    return list_of_properties

# def saving_datas(datas):
#      with open(test, 'a') as file:
#         json.dump(str(datas), file, indent=4)
#concurrency setting
# 1 driver by thread (we have four thread here)
drivers = [driversetting() for _ in range(2)]
#division of the number of pages by the number of threads 
division = np.array_split(np.arange(1,2),2)
#creation of a pool of threads
with ThreadPoolExecutor(max_workers=2) as executor :
    bucket = executor.map(scraping,division,drivers)
    results = [item for block in bucket for item in block]
    print(results)
