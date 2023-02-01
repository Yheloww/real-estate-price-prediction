import pandas as pd

def preprocess(path):
    """

    """
    column_final = ['number_bedrooms', 'living_area', 'fully_equipped_kitchen',
       'furnished', 'terrace', 'garden', 'facades_number', 'swimming_pool',
       'fire_place', 'provinces_Anvers', 'provinces_Brussel',
       'provinces_E.Flanders', 'provinces_F.Brabant', 'provinces_Hainaut',
       'provinces_Liege', 'provinces_Limbourg', 'provinces_Luxembourg',
       'provinces_Namur', 'provinces_W.Flanders', 'provinces_W.brabant',
       'type_property_apartement', 'type_property_house',
       'building_state_As new', 'building_state_Good',
       'building_state_Just renovated', 'building_state_To be done up',
       'building_state_To renovate', 'building_state_To restore']
    
    df1 = pd.read_json(path, typ='series').to_frame('values')
    df = df1.T
    list_data = df.columns.tolist()
    #changing type of column 
    df1 = df.convert_dtypes()
    #comparing two list of columns name
    for col in column_final:
        if col in list_data:
            if df1[col].dtype == "string":
                df1[col] = 1
            else:
                df1[col] = df[col]
        else :
            df1[col] = 0
    
    df1.replace({False: 0, True: 1}, inplace=True)

    df1 = df1[sorted(df1.columns)]
    print(df.values)
    return df1.values



import json, sys, os
