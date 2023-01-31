import json
import pandas as pd


#preprocess the data received in json 
"""
get the data in json 
-> transfrom it in pandas to preprocess
- get dummies 
- drop nan ... 
->get the y_pred out

keep just appartement and houses 
find a way to import csv empty (with 0 in the first row and all cols)
"""

def preprocess():
    """
    list of columns
    ['Price', 'Number_bedrooms', 'Living_area', 'fully_equipped_kitchen',
       'Furnished', 'terrace', 'garden', 'facades_number', 'Swimming_pool',
       'fire_place', 'provinces_Anvers', 'provinces_Brussel',
       'provinces_E.Fanders', 'provinces_F.Brabant', 'provinces_Hainaut',
       'provinces_Liege', 'provinces_Limbourg', 'provinces_Luxembourg',
       'provinces_Namur', 'provinces_W.Flanders', 'provinces_W.brabant',
       'Type_property_apartment', 'Type_property_house',
       'building_state_As new', 'building_state_Good',
       'building_state_Just renovated', 'building_state_To be done up',
       'building_state_To renovate', 'building_state_To restore']

    """
    df = pd.read_json('')
    cols = ['equipped_kitchen','furnished',
            'terrace','garden','swimming_pool','fire_place']
    for col in cols :
        df.loc[(df.col == False), col] = 0
        df.loc[(df.col == True), col] = 1

    dums = ['provinces', 'type_property', 'building_state']

    # for dum in dums:
    #     # find a way to create columns ? 
    #     df = pd.get_dummies(df, columns=[dum], drop_first=True)

    # X = df.drop(['Price'], axis=1).values

    return print(df.head)

preprocess()