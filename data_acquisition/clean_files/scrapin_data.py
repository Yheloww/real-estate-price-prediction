from get_links import *
import pandas as pd

def clean_data():

    list_of_link = "./links.txt"
    my_file = open(list_of_link, "r")
    for lk in my_file : 
        r = requests.get(lk)
        content = r.content
        property_details_page = BeautifulSoup(content,"html.parser")
        script_list = property_details_page.find_all("script")
        
    datas = organise_data(script_list)
    csv = save_to_csv(datas)
    return csv

def organise_data(scripts): 
    list_of_properties = []
    for script in scripts:  # iterate all the scripts to get relevent information

        # search for the script tag which have window.dataLayer in it, This script have most 
        # of the basic details that we need.

        if "window.dataLayer" in str(script): 
            script_content = str(script)
            details_json = json.loads(
                script_content[
                    script_content.index("[") : script_content.index("]") + 1
                ]
            )

        # search for the script tag which have window.classified in it, This script have some more 
        # information which we not found in previous script of the basic details that we need.
        
        if "window.classified" in str(script):
            script_content = str(script)
            facade_count = ""
            fireplace_exist = ""
            isFurnished = ""
            living_area = ""

            # It was defficult to parse this string to json because of the special character's, 
            # we have use split function to get required information from string.
            if '"facadeCount":' in script_content:
                facade_count = script_content.split('"facadeCount":')[1][
                    :2
                ].replace(",", "")
            if '"fireplaceExists":' in script_content:
                fireplace_exist = script_content.split('"fireplaceExists":')[1][
                    :5
                ].replace(",", "")
            if '"isFurnished":' in script_content:
                isFurnished = script_content.split('"isFurnished":')[1][:5].replace(
                    ",", ""
                )
            if '"netHabitableSurface"' in script_content:
                living_area = (
                    script_content.split('"netHabitableSurface":')[1]
                ).split(",")[0]

        element_locality = (script.find("span", class_="classified__information--address-row")
        if element_locality == None:
            .text.replace("\n", "")
            .strip()
            .replace("           ", "  ")
        )

        property_details = {}

        for key in ("type", "subtype", "price", "transactionType", "bedroom", "kitchen", "land", "building"):
            property_details[key.title()] = (
                None if details_json[0]["classified"][key] == "" else details_json[0]["classified"][key]
            )

        # Set property_details keys to 1 if the corresponding value in details_json[0]["classified"] is "true", else set the key to 0
        for key in ("isFurnished", "fireplace_exist", "garden", "terrace", "swimming_pool"):
            property_details[key.title()] = 1 if details_json[0]["classified"][key] == "true" else 0

        # Set property_details keys to the corresponding value in details_json[0]["classified"]
        # if the value is not an empty string, else set the key to None
        for key in ("locality", "surface_area", "living_area", "facade_count"):
            property_details[key.title()] = None if details_json[0]["classified"][key] == "" else details_json[0]["classified"][key]

        list_of_properties.append(property_details)
    print(list_of_properties)
    return list_of_properties

    

def save_to_csv(data): 

    datas = data
    df = pd.DataFrame(datas)
    df.replace("", None, inplace=True)

        # Saving the dataframe into a CSV file 
        # We specify mode (append) so the data will be appended into the csv file for every webpage we scrape
    
    return df.to_csv("property_data.csv", mode="a", header=None, index=False)
       