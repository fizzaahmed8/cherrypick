# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:59:27 2017

@author: Y40
"""
import string
import re
from feature_word import pos_neg

def sentence_pos(sentence, mode):
    """
    Args:
        sentence: string data
        mode: "normal" for bag-of-words, "revised" for revised bag-of-words, "upper2lower" for inserting a duplicate of capital words in its lower one case
    """
    words, upper_word, wordlist = cleanText(sentence,[],mode)
    return wordlist, upper_word
        
def cleanText(input_text, upper_list,mode):
    #input = bytes(input.encode('utf-8')) # 把内容转换成utf-8格式以消除转义字符
    if mode == 'revised':
        punctuation_reduced = string.punctuation[1:20] + string.punctuation[21:]
    if mode == 'normal':
        punctuation_reduced = string.punctuation
    if mode == 'upper2lower':
        punctuation_reduced = string.punctuation[1:20] + string.punctuation[21:]
    sequence = input_text.split(" ")
    for i in range(0,len(sequence)):
        item = sequence[i]
        if item.isupper() == True and len(item)>1:
            upper_list.append(item.strip(punctuation_reduced))
#        if mode == "upper2lower":
#            #print(i,item)
#            sequence.insert(i,item)
    input_text = re.sub('\n+'," ",input_text).lower() # 匹配换行,用空格替换换行符
    input_text = re.sub('\[[0-9]*\]', "", input_text) # 剔除类似[1]这样的引用标记
    input_text = re.sub(' +', " ", input_text) #  把连续多个空格替换成一个空格
    adj_list = []
    adj_str = ""
    input_text, word_freq, word_list = pos_neg(input_text, adj_list, adj_str, punctuation_reduced)
    #input = bytes(input)#.encode('utf-8') # 把内容转换成utf-8格式以消除转义字符
    #input = input.decode("ascii", "ignore")
    return input_text, upper_list, word_list
    
if __name__ == "__main__":
    sample_text = "The steak is very lovely while others may be very interested about it, the lemon juice is AWESOME. I mean, 20, CAN YOU BELIEVE what's happening right here??!!!"
    word_list, upperlist = sentence_pos(sample_text,'upper2lower')