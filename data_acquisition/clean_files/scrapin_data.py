from get_links import *
import pandas as pd

def clean_data():
    classified = []
    list_of_link = "./links.txt"
    my_file = open(list_of_link, "r")
    for lk in my_file : 
        print(lk)
        r = requests.get(lk)
        data_layer = []
        content = r.content
        property_details_page = BeautifulSoup(content,"html.parser")
        laye= property_details_page.find_all("script")[6]
        classi = property_details_page.find_all("script")[1]
        for script in laye:
            data_layer.append(script)
        for data in classi:
            data_layer.append(data)

        classified.append(data_layer)

        
    datas = organise_data(classified)
    csv = save_to_csv(datas)
    return csv

def organise_data(classified): 
    property_details = {}
    list_of_properties = []
    # use to store json which contains detailed information
    
    for script in classified[0]: 
        print(script)
        details_json = json.loads(
            script[
                script.index("[") : script.index("]") + 1
            ])
        property_details["Locality"] = (
            None
            if details_json[0]["classified"]["zip"] == ""
            else details_json[0]["classified"]["zip"]
        )
        property_details["Type_of_property"] = (
            None
            if details_json[0]["classified"]["type"] == ""
            else details_json[0]["classified"]["type"]
        )
        property_details["Subtype_of_property"] = (
            None
            if details_json[0]["classified"]["subtype"] == ""
            else details_json[0]["classified"]["subtype"]
        )
        property_details["Price"] = (
            None
            if details_json[0]["classified"]["price"] == ""
            else details_json[0]["classified"]["price"]
        )
        property_details["TransactionType"] = (
            None
            if details_json[0]["classified"]["transactionType"] == ""
            else details_json[0]["classified"]["transactionType"]
        )
        property_details["No_of_rooms"] = (
            None
            if details_json[0]["classified"]["bedroom"]["count"] == ""
            else details_json[0]["classified"]["bedroom"]["count"]
        )
        property_details["Kitchen"] = (
            0 if details_json[0]["classified"]["kitchen"]["type"] == "" else 1
        )
        property_details["Garden"] = (
            1
            if len(details_json[0]["classified"]["outdoor"]["garden"]["surface"]) != 0
            else 0
        )
        property_details["Terrace"] = (
            1
            if details_json[0]["classified"]["outdoor"]["terrace"]["exists"] == "true"
            else 0
        )
        property_details["Surface_area"] = (
            None
            if details_json[0]["classified"]["land"]["surface"] == ""
            else details_json[0]["classified"]["land"]["surface"] + "m2"
        )
        property_details["Swimming_pool"] = (
            0
            if details_json[0]["classified"]["wellnessEquipment"]["hasSwimmingPool"]
            == ""
            else 1
        )
        property_details["State_of_building"] = (
            None
            if details_json[0]["classified"]["building"]["condition"] == ""
            else details_json[0]["classified"]["building"]["condition"]
        )
        
        # search for the script tag which have window.classified in it, This script have some more 
        # information which we not found in previous script of the basic details that we need.
        
    # for win in data_layer : 
    #     script_content = str(win)
    #     facade_count = ""
    #     fireplace_exist = ""
    #     isFurnished = ""
    #     living_area = ""

    #     # It was defficult to parse this string to json because of the special character's, 
    #     # we have use split function to get required information from string.
    #     if '"facadeCount":' in script_content:
    #         facade_count = script_content.split('"facadeCount":')[1][
    #             :2
    #         ].replace(",", "")
    #     if '"fireplaceExists":' in script_content:
    #         fireplace_exist = script_content.split('"fireplaceExists":')[1][
    #             :5
    #         ].replace(",", "")
    #     if '"isFurnished":' in script_content:
    #         isFurnished = script_content.split('"isFurnished":')[1][:5].replace(
    #             ",", ""
    #         )
    #     if '"netHabitableSurface"' in script_content:
    #         living_area = (
    #             script_content.split('"netHabitableSurface":')[1]
    #         ).split(",")[0]
# property_details["Living_area"] = (
#             None if living_area == "" else living_area + "m2"
    # # first we take a specific html element that has the text of the locality
    # # and then we filter all the empty spaces and lines. That data is assigned into our property dataframe
    #     property_details["IsFurnished"] = 1 if isFurnished == "true" else 0
    #     property_details["Fireplace_exist"] = 1 if fireplace_exist == "true" else 0
    #     property_details["Facade_count"] = None if facade_count == "" else facade_count

        # if the value of the locality is empty on json then we are going to assign it as a None value 
        # otherwise it will copy the actual value and this is the way we filter all the other attributes of our dataframe

       
        

        # we are going to append the specific details of a property into the lists of properties

    list_of_properties.append(property_details)
    return list_of_properties

    

def save_to_csv(data): 

    df = pd.DataFrame(data)
    df.replace("", None, inplace=True)

        # Saving the dataframe into a CSV file 
        # We specify mode (append) so the data will be appended into the csv file for every webpage we scrape
    df.to_csv("property_data.csv", mode="a", header=None, index=False)

    return df

clean_data()