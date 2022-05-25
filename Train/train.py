# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
# P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
# Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn

import logging
from config import REPO

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

#Get URL from DVC
import dvc.api

path = 'data/train.csv'
repo = REPO
version = 'v1'

data_url = dvc.api.get_url(
                        path=path,
                        repo = repo,
                        rev = version)

mlflow.set_experiment('Test Demo')


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    #Read the csv file
    data = pd.read_csv(path)
    
    #Log Data Params
    mlflow.log_param("data_url", alpha)
    mlflow.log_param("data_version", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("input_rows", data.shape[0])
    mlflow.log_metric("input_columns", data.shape[1])

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "sales" which is a scalar from [3, 9]
    train_x = train.drop(["sales"], axis=1)
    test_x = test.drop(["sales"], axis=1)
    train_y = train[["sales"]]
    test_y = test[["sales"]]
    
    #Log Artifacts: columns used for modelling
    col_x = pd.DataFrame(list(train_x.columns))
    col_x.to_csv('features.csv', header=False, index=False)
    mlflow.log_artifact('features.csv')
    
    col_y = pd.DataFrame(list(train_y.columns))
    col_y.to_csv('target.csv', header=False, index=False)
    mlflow.log_artifact('target.csv')

    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    
    #Fitting the model
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
        
    #Perform prediction    
    predicted_qualities = lr.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
        