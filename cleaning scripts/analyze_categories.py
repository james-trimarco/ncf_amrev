#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:10:45 2019

@author: james
"""

import pandas as pd
import ast

input_filename = "/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/data/fine_foods_0313_joined.csv"

data = pd.read_csv(input_filename)

list(data.columns.values)

data[1:5,"categories"]

len(data.categories.unique())

# Goofing
counter = 0
firsts = []
seconds = []
for index, row in data.iterrows():
    if str(row['categories']) != 'nan':
        a = str(row['categories'])
        lst = ast.literal_eval(a)
        
        firsts.append(lst[0][0])
        
        if len(lst[0]) > 1:
            seconds.append(lst[0][1])
            
        else: 
            seconds.append('')
#        for idx, cat in enumerate(lst[0]):
#            if idx == 0:
#                firsts.append(cat)
#            if idx == 1:
#                seconds.append(cat)
                
    else:
        firsts.append('')
        seconds.append('')
                       
    counter += 1
    if counter == 2000:
        break






# [[x, firsts.count(x)] for x in set(firsts)]