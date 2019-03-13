import csv
import io
import re

###
# 1. Set up file locations
###
input_filename = "/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/amazon-meta.txt"
output_filename = "/Users/james/Documents/NCDS/Semester_2/Projects/AmRev/meta_test_output.csv"
 
   
###
# 2. Set up reader and csv writer.
###    
file = io.open(output_filename, 'w') 

csvOutInfo = open(output_filename, 'w', encoding='utf-8')
recordwriter = csv.writer(csvOutInfo, 
                          dialect = 'unix',
                          quotechar = '"',
                          quoting = csv.QUOTE_ALL)


###
# 3. Run script to process input. 
###

def find_between(s, first, last):
    """
    Extracts a substring from between two other substrings.
    """
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def correct_spacing(s):
    """
    Fixes two problems with periods in strings:
        - Period followed by a character
        - Period followed by multiple spaces
        - Makes exception for period surrounded by numerals
    """
    return re.sub(r'\.(?![ 0-9])', '. ', re.sub(r' +', ' ', s))

f = io.open(input_filename, 'r', encoding = 'utf_8', newline = '\n')
yourList = f.readlines()
        
for cell in yourList:      
    
    if cell[:5].strip() == 'ASIN:': # check for ASIN
        #import pdb; pdb.set_trace()
        productId = cell[5:] # Store the ASIN
    
    elif cell.strip()[:6] == 'title:':
        title = cell[9:]
        
    elif cell.strip()[:6] == 'group:':
        group = cell[9:]


        row = [productId, title, group]
        
        row = list(map(lambda x: x.rstrip('\n'), row))
    
        recordwriter.writerow(row)
            


                
