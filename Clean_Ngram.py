# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:22:08 2017

@author: Y40
"""

import re
import string
import operator

def cleanText(input, upper_list):
    #input = bytes(input.encode('utf-8')) # 
    punctuation_reduced = string.punctuation[1:20] + string.punctuation[21:]
    accentuate = string.punctuation[0]
    sequence = input.split(" ")
    for item in sequence:
        if item.isupper() == True and len(item)>1:
            upper_list.append(item.strip(punctuation_reduced))
    input = re.sub('\n+'," ",input).lower() 
    input = re.sub('\[[0-9]*\]', "", input) 
    input = re.sub(' +', " ", input) 
    #input = bytes(input)#.encode('utf-8') 
    #input = input.decode("ascii", "ignore")
    return input, upper_list

def weight(word_list, upper_list):
    return []
    
def cleanInput(input,upper_list):
    input, upper_list = cleanText(input, upper_list)
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation) # string.punctuation
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput,upper_list

def getNgrams(input, n, upper_list):
    input, upper_list = cleanInput(input, upper_list)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])#.encode('utf-8')
        if ngramTemp not in output: 
            output[ngramTemp] = 0 
        output[ngramTemp] += 1
    weight_list = weight(output, upper_list)
    return output, upper_list, weight_list
    
    
if __name__ =="__main__":
    import pandas as pd
    user_data = pd.read_csv("D:\\Desktop\\Material\\STAT 154\\Kaggle\\ShrinkedData\\cherrypick_academic_dataset_review_train.csv")
    str_sample = user_data.loc[[3]].text.values[0]
    upperList = []    
    #clean_text, upperList = cleanInput(str_sample, upperList)
    output, upperList = getNgrams(str_sample,3, upperList)
