
import pandas as pd
import json
import ast 

import requests
from bs4 import BeautifulSoup


list_of_link = ['https://www.immoweb.be/en/classified/house/for-sale/ronse/9600/10315915', 'https://www.immoweb.be/en/classified/house/for-sale/laeken/1020/10313082' ]
list_of_properties = []
for lk in list_of_link:
    print(lk)
    r = requests.get(lk)
    content = r.content
    property_details_page = BeautifulSoup(content, "html.parser")
    info = property_details_page.find_all(class_ = 'classified-table__data')
    print(info)
    # datalayer = property_details_page.find_all("script")[1]
    # classified = property_details_page.find_all("script")[6]
    # text = classified.text
    # ids = classified.find("customers")
    # print(ids)

    #print(res)


