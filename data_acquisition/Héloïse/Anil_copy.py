from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import pandas as pd

for i in range(1, 2):
    page_num = str(i) + "&orderBy=relevance"
    url = (
        "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page=" + page_num
    )
    list_of_properties = []
    # I'm giving a break because it needs 
    time.sleep(30)  

    driver = webdriver.Chrome(executable_path="driver/chromedriver")
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html.parser")


    listings = soup.find_all("a", class_="card__title-link")

    for pages in listings:  

        list_of_properties.append(pages["href"])
        property_details = {}
        driver.get(pages["href"]) # get the response from the url
        property_details_page = BeautifulSoup(driver.page_source, "html.parser")

    #print(list_of_properties)
    print(property_details_page)

