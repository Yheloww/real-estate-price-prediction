import numpy as np

division = np.array_split(np.arange(1,300),4)
print(division)


provinces = ['liege', 'bruxelles']
page_num = 0

for province in provinces : 
    url = (f"https://www.immoweb.be/fr/recherche/maison/a-vendre/{provinces}/province?countries=BE&page={page_num}&orderBy=relevance")
    
