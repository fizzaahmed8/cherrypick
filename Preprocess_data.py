# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:41:09 2017

@author: Y40
"""
from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import ensemble
from sklearn import metrics
from sklearn import neural_network
from sklearn import decomposition

from data_SVM import SVM
user_data = pd.read_csv("./data/yelp_academic_dataset_review_train.csv")

# load the data
load_num = 1000
load_data = user_data.loc[[i for i in range(0,load_num)]]
                           
business_list_list = [] 

business_id = []
funny_id = []
cool_id =[]
useful_id = []
date = []
review_num = []
star_list = []
star_whole = []
review_whole = []
busi_review_temp = []
busi_date_temp = []
busi_star_temp =[]
busi_id_temp = 'Haliluya'
for i in range(0,load_num):
    data_temp = user_data.loc[[i]]
    if user_data.loc[[i]]['business_id'].values[0] not in business_id:
        busi_id = user_data.loc[[i]]['business_id'].values[0]
        business_id.append(busi_id)
        
        #print("#review:",len(busi_review_temp))
        review_num.append(len(busi_review_temp))
        #print("#date:",len(busi_date_temp))
        
        if len(busi_review_temp) > 0 and busi_id != busi_id_temp:
            business_list_list.append(busi_review_temp)
            date.append(busi_date_temp)
            star_list.append(busi_star_temp)
            
        #initialize
        busi_id_temp = busi_id
        busi_review_temp = []
        busi_date_temp = []
        busi_star_temp =[]
        
    busi_id_temp = data_temp['business_id'].values[0]
    busi_review_temp.append(data_temp.text.values[0])
    busi_date_temp.append(data_temp.date.values[0])
    busi_star_temp.append(data_temp.stars.values[0])
    review_whole.append(data_temp.text.values[0])
    star_whole.append(data_temp.stars.values[0])

# Bag of words
def review_to_words( review_text ):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and 
    # the output is a single string (a preprocessed movie review)
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))
    
# bag of words part
clean_train_reviews = []
for elem in review_whole:
    a = review_to_words(elem)
    clean_train_reviews.append(a)
print("get the meaningful words")
from sklearn.cross_validation import train_test_split
from sklearn import svm

clean_train_reviews = []
for elem in review_whole:
    a = review_to_words(elem)
    clean_train_reviews.append(a)

#Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.  
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 1000) 

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of 
# strings.
train_data_features = vectorizer.fit_transform(clean_train_reviews)

# Numpy arrays are easy to work with, so convert the result to an 
# array
train_review_features = train_data_features.toarray()
print(train_review_features.shape)
train_star = np.array(star_whole)

# PCA
pca = decomposition.PCA(n_components=50)
train_review_features = pca.fit_transform(train_review_features)

# Shuffle the tarining set and validation set
print("Shuffle the data")
review_train, review_test, star_train, star_test = train_test_split(train_review_features, train_star, test_size=0.2, random_state=0)

# Fit linear regression on the model
# print("SVM")
# model = SVM(review_train,star_train,review_test,star_test)

# Ensemble Methods
rf = ensemble.RandomForestClassifier(n_estimators=30, max_features=20, max_depth=5)
rf.fit(review_train, star_train)

pred_train = rf.predict(review_train)
pred_test = rf.predict(review_test)

# Neural Network
# nn = neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
# nn.fit(review_train, star_train)

# pred_train = nn.predict(review_train)
# pred_test = nn.predict(review_test)

# print(pred_train[:100])
# print(pred_test[:100])

print("Training accuracy: %f" % metrics.accuracy_score(pred_train, star_train))
print("Test accuracy: %f" % metrics.accuracy_score(pred_test, star_test))
