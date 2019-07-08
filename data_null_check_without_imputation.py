# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

def impute_to_null(val,col):
    index = 0
    pos=0
    mean = 0
    temp_arr=list(val[col])
    
    for x in temp_arr:
        if str(x) == 'nan':
            pos = index
        else:
            mean += x
        index+=1
    mean = mean/(index-1)
    temp_arr[pos]= mean
    return temp_arr
    

def get_data():
    headers=['sepal_len','sepal_width','petal_len','petal_width','class']
    df = pd.read_csv('DataForAlgo/myTestData.csv', header=None,names=headers)
    return df

if __name__ == '__main__':
    df = get_data()
    X=df.iloc[:,:-1]
    print(X)
    colname = X.columns
    for col in colname:
        if X[col].isnull().sum() == 1:
            X[col] = impute_to_null(X,col)
    print("=================================\n",X)