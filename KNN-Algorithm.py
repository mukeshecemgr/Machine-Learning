import csv
import random

def split_train_test_set(dataset,split,train_data=[],test_data=[]):
    '''Separating training and test set'''
    for x in range(len(dataset)-1):
        for y in range(4):
            dataset[x][y]=float(dataset[x][y])
        if random.random() < split:
            train_data.append(dataset[x])
        else:
            test_data.append(dataset[x])


def load_iris_data():
    '''Loading iris data from file'''
    split=0.66
    with open('/Users/mukeshgupta/Documents/GitHub/Machine-Learning/iris/iris.data','r') as iris_data:
        lines = csv.reader(iris_data)
        dataset=list(lines)
        train_data=[]
        test_data=[]
    
        split_train_test_set(dataset,split,train_data,test_data)
    print(repr(len(train_data)))
    print(repr(len(test_data)))
    

def KNN_Start():
    '''KNN algorithm raw'''
    load_iris_data()
    

       
if __name__ == '__main__' :
    KNN_Start()