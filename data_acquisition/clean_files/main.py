from get_links import *
from threads import * 
from scrapin_data import *

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json
import requests
import numpy as np
from concurrent.futures import ThreadPoolExecutor

test = f"./links.txt"



def main():
    #getting the link 
    try : 
        pool(2,4)
        clean_data()

    except : 
        pass 


main() 
