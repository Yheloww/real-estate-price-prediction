from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json
import requests
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# destination file of the URLs collected
test = f"./links.txt"

# driver init
def driver_gen():
    driver = webdriver.Firefox()
    return driver

# detect if the page contains a pagination
def pagination(search_page)
    has_pagination = search_page.find("class":"pagination")
    if has_pagination == -1:
        page_exists = False
    else:
        page_exists = True
    return page_exists

# open immoweb using selenium and add the links of announces into a list
def get_links(iterations, driver):
    list_of_link = []
    provinces = ["antwerp", "brabant", "brussels", "west-flanders", "east-flanders", "hainaut", "liege", "limburg", "luxembourg", "namur"]

    for prov in range(len(provinces)):
        province=provinces[prov]
    
        for num in iterations:
            page_num = str(num)
            url = (
                    "https://www.immoweb.be/en/search/house-and-apartment/for-sale/"+province+"/pronvince?countries=BE&page="+page_num+"&orderBy=relevance"
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

# save the list of links into an external file
def link_file(datas):
    with open(test, 'a') as file:
        file.write(f'{datas}\n')