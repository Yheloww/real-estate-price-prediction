#first we import every libraries that we need
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json
import requests
import numpy as np
from concurrent.futures import ThreadPoolExecutor
#then we create the file were the datas are gonna go
test = f"./links.txt"
#we initiate the driver for the selenium part
def driver_gen():
    driver = webdriver.Chrome(executable_path="driver/chromedriver")
    return driver


def get_links(iterations, driver):
    list_of_link = []
    #still doing by page number is gonna change
    for num in iterations:
        page_num = str(num) + "&orderBy=relevance"
        url = (
                "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page=" + page_num
                )
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        dict_of_informations = {}
        for link in soup.find_all("a", class_="card__title-link") : 
            list_of_link.append(link['href'])
            #print(link['href'])
    driver.quit()
    #calling clean function to clean and return clean data
    #not the good way i think incorporate links finding in data cleaning
    print(len(list_of_link))
    return list_of_link

def link_file(datas):
    with open(test, 'a') as file:
        file.write(f'{datas}\n')