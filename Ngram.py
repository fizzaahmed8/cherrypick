# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:16:57 2017

@author: Y40
"""
import nltk
import string
#from nltk.model import NgramModel
from nltk.probability import LidstoneProbDist
from nltk.tokenize import word_tokenize

def function():
    pass






if __name__=='__main__':
    import pandas as pd
    user_data = pd.read_csv("D:\\Desktop\\Material\\STAT 154\\Kaggle\\ShrinkedData\\yelp_academic_dataset_review_train.csv")
    load_num = 200
    str_sample = ""
    for i in range(0,load_num):
        str_sample = str_sample + user_data.loc[[i]].text.values[0]
    punctuation_reduced = string.punctuation[1:20] + string.punctuation[21:]
    corpus = word_tokenize(str_sample.strip(punctuation_reduced))
    
    # Train on 90% f the corpus and test on the rest
    spl = int(90*len(corpus)/100)
    train = corpus[:spl]
    test = corpus[spl:]
    fdist = nltk.FreqDist(w for w in train)
    
    