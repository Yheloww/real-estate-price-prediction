from model_train import * 
from preprocessing import *

PATH_RAW = r'C:\Users\feldm\Documents\GitHub\real-estate-price-prediction\data\raw.csv'

def preprocess_ensemble(): 
    """
    function to unite every function in preprocessing
    """


def main():
    # getting the dataFrame
    get_raw_data(PATH_RAW)
    # process the datas
    Path = preprocess_ensemble()
    # train and evaluate 
    X_train,X_test, y_train, y_test = get_X_y(Path, "Price")

    evalutation = eval_model(X_train,X_test, y_train, y_test)
         
    return evalutation


if __name__ == "__main__":
    main() 