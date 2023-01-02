from bs4 import BeautifulSoup
import requests
import json

url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=2&orderBy=relevance"
r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
content = r.content
print(content)
links = []
for elem in soup.find_all("li", ):
    print(elem.get("href"))
    # test = elem.text
    # links.append(test)
for elem in soup.find_all("a", id="card__title-link") :
    print(elem)
    print(elem.get("id href"))



# test = f"./datas.json"
# with open(test, 'w') as file:
#     json.dump(links, file, indent=4)


