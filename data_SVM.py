# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:53:48 2017

@author: Y40
"""
from sklearn.svm import SVC
def SVM(train_x,train_y,test_x,test_y):
    clf = SVC()
    clf.fit(train_x, train_y) 
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
        decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
        max_iter=-1, probability=False, random_state=None, shrinking=True,
        tol=0.001, verbose=False)
    
    # Validation data
    review_validation_result = clf.predict(test_x)
    misClass = 0
    for i in range(0,len(test_y)):
        if review_validation_result[i]!=test_y[i]:
            misClass = misClass + 1
    accurarcy = 1 - (misClass/len(test_y))
    l1accurarcy = sum(abs(review_validation_result-test_y))
    print("Acurarcy:",accurarcy)
    print("L1 Accurarcy: ",l1accurarcy/len(test_y))
    return clf