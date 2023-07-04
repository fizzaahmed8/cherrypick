# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:41:09 2017

@author: Y40
"""
from __future__ import division
import pandas as pd
import numpy as np
#import matplotlib.dates as mdates
#import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from data_SVM import SVM
from sklearn.cross_validation import train_test_split
from feature_tag import sentence_pos
import time

user_data = pd.read_csv("D:\\Desktop\\Material\\STAT 154\\Kaggle\\ShrinkedData\\yelp_academic_dataset_review_train.csv")
data_test = pd.read_csv('D:\\Desktop\\Material\\STAT 154\\Kaggle\\ShrinkedData\\yelp_academic_dataset_review_test.csv')
#all_reviews = pd.concat([pd.DataFrame(clean_train_reviews), data_test.text])
train_length = user_data.shape[0]
test_length = data_test.shape[0]
all_reviews = pd.concat([user_data.text, data_test.text])
print("File has been read")
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
    #letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # 3. Convert to lower case, split into individual words
    #words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    words, upper_word = sentence_pos(review_text, 'revised')
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    #return meaningful_words, ( " ".join( meaningful_words )), upper_word
    return (" ".join( meaningful_words )), upper_word
    
# bag of words part
clean_train_reviews = []
clean_test_reviews = []
upper_list_train = []
upper_list_test = []
#for elem in review_whole:
#for elem in all_reviews:
#    a, upperword = review_to_words(elem)
#    upper_list = upper_list + upperword
#    clean_train_reviews.append(a)
dim = min(train_length,test_length)
for i in range(0,dim): # Not all the data of train is used
    elem = all_reviews.loc[[i]]
    a, upperword = review_to_words(elem.values[0])
    b, upperword_test = review_to_words(elem.values[1])
    upper_list_train = upper_list_train + upperword
    upper_list_test = upper_list_test + upperword_test
    clean_train_reviews.append(a)
    clean_test_reviews.append(b)


print("get the meaningful words")

#Initialize the "CountVectorizer" object, which is scikit-learn's

# bag of words tool.  
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 700) 


#all_reviews = pd.concat([pd.DataFrame(clean_train_reviews), data_test.text])
#train_data_features = vectorizer.fit_transform(clean_train_reviews) # list of strings
X_counts = vectorizer.fit_transform(clean_train_reviews + clean_test_reviews)
train_data_features = X_counts[:dim]
X_test_counts = X_counts[dim:]

# Numpy arrays are easy to work with, so convert the result to an 
# array
train_review_features = train_data_features.toarray()
print(train_review_features.shape)
#train_star = np.array(star_whole)
train_star = np.array(user_data.stars)[:min(train_length,dim)]
# Shuffle the tarining set and validation set
print("Shuffle the data")
review_train, review_test, star_train, star_test = train_test_split(train_review_features, train_star, test_size=0.2, random_state=0)

# Fit linear regression on the model
print("SVM")
model, validation_y = SVM(review_train,star_train,review_test,star_test)

# Predict the data
preds = model.predict(X_test_counts.toarray())
data_test["preds"] = preds
pred_per_buisiness = data_test.groupby("business_id").mean().preds
test_biz = pd.read_csv("D:\\Desktop\\Material\\STAT 154\\Kaggle\\ShrinkedData\\yelp_academic_dataset_business_test.csv")
pred_df = pd.DataFrame([{"business_id": biz, "stars": pred_per_buisiness[biz]} for biz in set(test_biz.business_id)])
pred_df = pred_df.set_index("business_id")
#pred_df.to_csv("Submission" + time.strftime('%Y-%m-%d %H:%M:%S  UTC%z',time.localtime(time.time())))
pred_df.to_csv("Submission_2.csv")
print("Prediction done")