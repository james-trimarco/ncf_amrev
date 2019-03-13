#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:21:53 2019

@author: james
"""
import io
import re
import csv

input_file = "/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/metadata.py"
output_filename = "/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/parsed_metadata.csv"

csvOutInfo = open(output_filename, 'w', encoding='utf-8')
recordwriter = csv.writer(csvOutInfo, 
                          dialect = 'unix',
                          quotechar = '"',
                          quoting = csv.QUOTE_MINIMAL)

rx_dict = {
    'productId': re.compile(r"(?<='asin': ').*?(?=',\s)"), # get productId
    'title': re.compile(r"(?<='title': '|'title': \").*?(?=(',\s)|(\",\s)|('})|(\"}))"), # get product title
    'categories': re.compile(r"(?<='categories':).*?(\]\])") # get product categories
    
}


def parse_file(file_path):
    """
    Parse malformed JSON file at given filepath

    Parameters
    ----------
    filepath : str
        Filepath for file_object to be parsed
        
    Returns
    ----------
    Writes rows to a specified csv file. 

    """
    
    header = ["productId", "title", "categories"] # create list of data
    recordwriter.writerow(header) # write data to csv

    # open the file and read through it line by line
    with io.open(input_file, 'r', encoding = 'utf-8') as file_object:
        for line in file_object.readlines():
            #import pdb; pdb.set_trace()
            
            productId, title, categories = '', '', ''

            # check for productId
            if rx_dict['productId'].search(line):
                pmatch = rx_dict['productId'].search(line)
                productId = pmatch.group().strip()
            
            # check for title
            if rx_dict['title'].search(line):
                tmatch = rx_dict['title'].search(line)
                title = tmatch.group().strip()
                
            # check for categories
            if rx_dict['categories'].search(line):
                cmatch = rx_dict['categories'].search(line)
                categories = cmatch.group().strip()
            
            row = [productId, title, categories] # create list of data
            recordwriter.writerow(row) # write data to csv
        
parse_file(input_file)



