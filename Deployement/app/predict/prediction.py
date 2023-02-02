import pickle
import json
import pandas as pd
import numpy as np
from preprocessing.cleaning_data import preprocess

def predict(path):
    """
    
    """
    X_test = preprocess(path)
    print(X_test.shape)
    pickled_model = pickle.load(open('./predict/model.pkl', 'rb'))
    #
    m = pickled_model.predict(X_test) 
    rounded_up_integer_array = (np.ceil(m)).astype(int)

    return rounded_up_integer_array
