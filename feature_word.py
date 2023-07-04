# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:18:25 2017

@author: Y40
"""
import re
import nltk
from collections import deque
import string

def pos_neg(raw_str, adj_list, adj_str, punctuation):
    """ Extract the adjectives(in the reviews are very likely to have positive and negtive meaning towards the resteraunt )
    
    Args:
        
        raw_str: string of unprocessed text
        
        adj_list: list of adjectives
        
        adj_str: string of adjecitves
        
        punctuation: list of punctuations to take out
            
    Return:
        
        adj_list: list of adjectives
        
        tags: high frequent adjectives in all the sentences
        
        word_list: processed list of tokenized sentences
        
    """
    word_str = re.sub("[\s+\.\/_,$%^*()+\"\']+|[+——，。、@#￥%……&*（）【】：；:]", " ",raw_str)
    word_str = word_str.replace('！',' ！').replace('？',' ？').replace('!',' !').replace('?',' ?').replace('~',' ~')
    word_str = re.sub(' +', " ", word_str)
    word_list = word_str.split()
    #print(word_list)
    window = min(4, len(word_list))
    pre_word = deque(maxlen = window)
    pre_word.append(['','start'])
    adj_temp = ['start',0]
    zg_temp = ['start',0]
    token_list = nltk.pos_tag(word_list)
    for i in range(0,len(token_list)):
        w = token_list[i]
        pre_word.append(list(w))
        if w[1] == '.':
            zg_temp = (list(w),i)
        if w[1] == 'JJ':
            adj_temp = (list(w),i) # i is the position of the word
            adj_list.append(w[0])
            adj_str = adj_str + w[0]
        if zg_temp[0] in pre_word:
            word_list.insert(zg_temp[1],w[0])
            del word_list[zg_temp[1]]
        if (w[0] == '!' or '?' or '~') and adj_temp[0] in pre_word:
            del word_list[i]
            word_list.insert(adj_temp[1],adj_temp[0][0])
        if w[1] == 'NN' and adj_temp[0] in pre_word:
             word_list.insert(i,w[0])
        tags = nltk.FreqDist(word_list)
    return adj_list, tags, word_list
    
if __name__ =="__main__":
    sample_text = "The steak is very lovely while others may be very interested about it, the lemon juice is AWESOME. I mean, 20, CAN YOU BELIEVE what's happening right here??!!!(right, things becomes easier?!)OOhh~ Yeah"
    adj_list, word_freq, wordlist = pos_neg(sample_text, [], "", string.punctuation)