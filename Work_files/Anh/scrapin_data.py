from get_links import *


def clean_data():
    house_number = 1
    dict_of_informations= {}
    list_of_link = "./links.txt"
    my_file = open(list_of_link, "r")
    for lk in my_file : 
        r = requests.get(lk)
        content = r.content
        property_details_page = BeautifulSoup(content,"html.parser")
        dict_of_data= {}
        #we clean the datas by finding tags
        for tr in property_details_page.find_all('tr', attrs={'class':'classified-table__row'}):
            #these are the tage were our infos are
            value = tr.find('th')
            data = tr.find('td')
            if value != None :
                #we clean them using regex yay !
                title = re.sub(r'\s*<[^>]*>\s*','',str(value))
                if data != None : 
                    datas = re.sub(r'\s*<[^>]*>\s*','',str(data))
                    # we delete the big space to replace them with 1 only
                    datass = " ".join(datas.split())
                    #we store data in the dict
                    dict_of_data[title] = datass
                else: 
                    #if there are no datas we write none
                    dict_of_data[title] = None
            else: 
                continue
        #we put the datas in a another dict with all the house listed
        

        dict_of_informations[house_number] = dict_of_data
        house_number += 1 
    print(dict_of_informations[1])
    print(dict_of_informations[2])
    return dict_of_informations
    #right now the data is are dictionaries in a dictionary

clean_data()