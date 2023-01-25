import pandas as pd
import numpy as np 

def get_raw_data(path : str):

    df = pd.read_csv(r'C:\Users\feldm\Documents\GitHub\real-estate-price-prediction\data\raw.csv')
    return df 

def replace_NAN(cols : list, df):

    """
    sometimes NAN needs to be replace by mean or 0 value. 
    The list of col is th columns that needs to be replace and not dropped
    """
    df.replace(to_replace="None", value=np.nan, inplace=True)

    for col in cols: 
        df['col'].fillna(0, inplace=True)


def drop_nan(cols : list):

    """
    find the percentage of nan in each columns if nan is more than a certain percentage drop col 
    else drop rows from the concerned col 
    """

def change_types(df, cols : list):

    """
    check content of eahc columns and the matching type, if the type doesnt match, change it in the right type 

    """
    for col in cols : 
        if pd.to_numeric(df['col']):
            df['col'] = pd.to_numeric(df['col'])

        else: 
            df['col'] = df['col'].astype('string')



def create_col(col : str, df):

    """
    create a new columns based on other columns 
    """
    df["provinces"] = df["col"]
    df['provinces'] = np.where(df['locality'].between(1000,1299), "Brussel", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(6600,6999), "Luxembourg", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(2000,2999), "Anvers", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(1300,1499), "W.brabant", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(7000,7999), "Hainaut", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(6000,6599), "Hainaut", df['provinces'])

    df['provinces'] = np.where(df['locality'].between(3500,3999), "Limbourg", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(5000,5680), "Namur", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(9000,9999), "E.Fanders", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(1500,1999), "F.Brabant", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(3000,3499), "F.Brabant", df['provinces'])

    df['provinces'] = np.where(df['locality'].between(8000,8999), "W.Flanders", df['provinces'])
    df['provinces'] = np.where(df['locality'].between(4000,4999), "Liege", df['provinces'])

def remove_outliers(cols : list): 

    """
    find outliers and 
    remove the outliers of float or str type cols
    """
    for col in cols : 
        p25 = df['col'].quantile(0.25)
        p75 = df['col'].quantile(0.75)
        iqr = p75-p25
        upper_limit = p75 + 1.5 * iqr
        lower_limit = p25 - 1.5 * iqr
        df= df.drop(df[df['col'] > upper_limit].index)
        df= df.drop(df[df['col'] < lower_limit].index)
        

def get_dummies(cols : list):
    """
    
    """