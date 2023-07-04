# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:09:55 2017

@author: Y40
"""
import numpy as np
import math

def MSE(vec_test,vec_pred,mode):
    """ 
    Args:
        vec_test: the vector of test data
        vec_pred: the vector of prediction data
        mode: choose "MSE" or "RMSE"
    """
    mse = np.linalg.norm(vec_test-vec_pred,2)**2
    if mode == 'MSE':
        return mse/len(vec_test)
    if mode == 'RMSE':
        return math.sqrt(mse)/len(vec_test)
    
def L1_accurarcy(vec_test,vec_pred):
    l1accurarcy = sum(abs(vec_test-vec_pred))/len(vec_test)
    return l1accurarcy
    
def misClass(vec_test,vec_pred):
    misClass = 0
    for i in range(0,len(vec_test)):
        if vec_pred[i]!=vec_test[i]:
            misClass = misClass + 1
    misClassification = misClass/len(vec_test)
    return misClassification
    
    
if __name__ == "__main__":
    vector_pred = np.array([0,1,2,3])
    vector_test = np.array([0,0,0,0])
    mse = MSE(vector_pred,vector_test,'MSE')
    rmse = MSE(vector_pred,vector_test,'RMSE')
    l1accu = L1_accurarcy(vector_pred,vector_test)
    misClass = misClass(vector_pred,vector_test)
    print(" MSE:",mse,
          "\n RMSE:",rmse,
          "\n L1 accurarcy:",l1accu,
          "\n misClass:", misClass)