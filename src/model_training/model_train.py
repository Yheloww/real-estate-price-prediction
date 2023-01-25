import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error


from sklearn.pipeline import Pipeline

PATH = r'C:\Users\feldm\Documents\GitHub\real-estate-price-prediction\data\preprocessed.csv'


def get_dataframe(Path : str):
    """

    """
    df = pd.read_csv(Path)
    return df 


def get_X_y(PATH, test : str):
    """
    
    """
    df = get_dataframe(PATH)

    y = df[test].values
    X = df.drop(test,axis=1).values

    X_train,X_test, y_train, y_test = train_test_split(X,y,random_state=15)

    return X_train,X_test, y_train, y_test


def model_training(X_train, y_train):
    """
    
    """
    steps=[("scale", StandardScaler()),
        ("model", GradientBoostingRegressor(n_estimators=500, learning_rate=0.1, max_depth=9))]

    pipe = Pipeline(steps)
    pipe.fit(X_train,y_train)
    print("model trained")
    return pipe 

def eval_model(X_train,X_test, y_train, y_test):
    """
    
    """
    pipe = model_training(X_train,y_train)

    y_pred = pipe.predict(X_test)

    r2 = r2_score(y_test, y_pred)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    mape = mean_absolute_percentage_error(y_test,y_pred)


    return f"r2 score is {r2}, the rsquared error is {rmse}, the mean absolute error % is {mape} "


X_train,X_test, y_train, y_test = get_X_y(PATH, "Price")

print(eval_model(X_train,X_test, y_train, y_test))