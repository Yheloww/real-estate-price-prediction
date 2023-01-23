import pandas as pd
import numpy as np 

def get_dataframe(path : str):

    df = pd.read_csv(path)
    return df 

def replace_NAN(cols : list):

    """
    sometimes NAN needs to be replace by mean or 0 value. 
    The list of col is th columns that needs to be replace and not dropped
    """

def drop_nan(cols : list):

    """
    find the percentage of nan in each columns if nan is more than a certain percentage drop col 
    else drop rows from the concerned col 
    """

def change_types():

    """
    check content of eahc columns and the matching type, if the type doesnt match, change it in the right type 

    """

def create_col(col : str):

    """
    create a new columns based on other columns 
    """

def remove_outliers(col : list): 
    
    """
    remove the outliers of float or str type cols
    """