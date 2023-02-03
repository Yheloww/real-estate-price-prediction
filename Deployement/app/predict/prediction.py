import pickle
import numpy as np
from preprocessing.cleaning_data import preprocess


def predict(path):
    """
    predict the price with the parameter of the form

    Parameter:
        path : the path to the json file with the infos 

    Returns: 
        result : the rounded price that has been predicted by the model

    """
    # the data goes to the function that get the data ready
    X_test = preprocess(path)
    # importation of the model via pickle (see src/model_training/model_train.py)
    pickled_model = pickle.load(open('./predict/model.pkl', 'rb'))
    # prediction
    m = pickled_model.predict(X_test)
    # rounding and changing the type of the result
    results = (np.ceil(m)).astype(int)

    return results
