import pickle
from predict import prediction

"""
import the code of the model maybe pipeline and everything
output the model, find way to get the trained model out ? 

"""
path = 'path to json file'

def predict(path):
    """
    
    """
    X_test = prediction.preprocess(path)
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    #
    return pickled_model.predict(X_test)