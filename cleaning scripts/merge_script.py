#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:04:42 2019

@author: james
"""

import csv
import pandas as pd
import numpy as np

reviews = pd.read_csv("/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/data/fine_foods_0313A.csv", 
                      encoding = "ISO-8859-1")

#metadata = pd.read_csv("/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/data/amrev_metadata.csv")

metadata = pd.read_csv("/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/data/parsed_metadata.csv")

df3 = reviews.merge(metadata, on="productId", how='left')
df3.to_csv("/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/data/joined.csv",index=False)