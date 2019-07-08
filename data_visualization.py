# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

def impute_to_null(val):
    index = 0
    for x in val:
        if x != 0:
            print(x)

def get_data():
    headers=['sepal_len','sepal_width','petal_len','petal_width','class']
    df = pd.read_csv('DataForAlgo/myTestData.csv', header=None,names=headers)
    return df

if __name__ == '__main__':
    df = get_data()
    X=df.iloc[:,:-1]
    colname = X.columns
  #  print(colname)
  #  colname = X.isnull().sum().sort_values(ascending=False)
    for i in colname:
        if X[i].isnull().sum() == 1:
            X[i] = impute_to_null(X[i])