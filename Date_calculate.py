# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:30:41 2017

@author: Y40
"""
import csv
import pandas as pd
import datetime

def date_calculate(start_date,date,mode):
    if mode == 'str':
        year1,month1,day1 = start_date.split('-')
        year1 = year1.split(' ')[-1]
        year2,month2,day2 = date.split('-')
        year2 = year2.split(' ')[-1]
        interval = (datetime.datetime(int(year2), int(month2), int(day2))-datetime.datetime(int(year1), int(month1), int(day1))).days
        
    if mode == 'list':
        year1 = start_date[0]
        month1 = start_date[1]
        day1 = start_date[2]
        year2 = date[0]
        month2 = date[1]
        day2 = date[3]
        interval = (datetime.datetime(int(year2), int(month2), int(day2))-datetime.datetime(int(year1), int(month1), int(day1))).days
    print(year1,month1,day1)
    print(year2,month2,day2)
    return interval
    
def date_add_sort(TotalList,date):
    TotalList.append(date)
    TotalList.sort(key=lambda x: x.split('-'))
    return TotalList
    
if __name__=='__main__':
    user_data = pd.read_csv("D:\\Desktop\\Material\\STAT 154\\Kaggle\\ShrinkedData\\yelp_academic_dataset_review_train.csv")
    datee = user_data.loc[[1]].date.values[0]
    datee2 = user_data.loc[[2]].date.values[0]
    datee3 = user_data.loc[[3]].date.values[0]
    print(datee,datee2,datee3)
    interval = date_calculate(datee,datee2,'str')
    print(interval)
    dateList = [datee,datee2,datee3]
    dateList.sort(key=lambda x: x.split('-')) 
    print(dateList)