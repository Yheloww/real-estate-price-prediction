from bs4 import BeautifulSoup
import requests

url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=2&orderBy=relevance"
r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
content = r.content

links = []
for elem in soup.find_all("div", attrs={"class": "results"}):
    print(elem)
