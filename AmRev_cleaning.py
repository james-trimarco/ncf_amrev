import csv
import io
import re

###
# 1. Set up file locations
###
input_filename = "/Users/james/Desktop/finefoods.txt"
output_filename = "/Users/james/Desktop/sm_output_test.csv"
 
   
###
# 2. Set up reader and csv writer.
###    
file = io.open(output_filename, 'w') 

csvOutInfo = open(output_filename, 'w', encoding='utf-8')
recordwriter = csv.writer(csvOutInfo, 
                          dialect = 'unix',
                          quotechar = '"',
                          #escapechar = '\\',
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

f = io.open(input_filename, 'r', encoding = 'latin-1', newline = '\n')
yourList = f.readlines()
        
for cell in yourList:      
    
    
    if cell[:11] == 'product/pro': # check for productId
        productId = cell[19:] # Store the productId
    
    elif cell[:11] == 'review/user':
        userId = cell[14:]
        
    elif cell[:11] == 'review/prof':
        profileName = cell[20:]
        
    elif cell[:11] == 'review/help':
        # break helpfulness into numerator & denominator
        help_num, help_den = cell[20:].split('/')    
          
    elif cell[:11] == 'review/scor':
        score = cell[14:]
    
    elif cell[:11] == 'review/time':
        time = cell[13:]
        
    elif cell[:11] == 'review/summ':
        summary = cell[16:]
        
    elif cell[:11] == 'review/text':
        text = cell[13:]
        
        if 'Length::' in text: # extract seconds
            v = re.findall(r"::\s([^\"]+)\sMins", text) # extract video length
            v_str = re.sub('[\'\[\]]', '', str(v)) # convert to string and remove brackets
            v_list = v_str.split(':')
            vid_length = str(int(v_list[0])*60 + int(v_list[1])) # convert to total seconds
            text = re.sub(r"Length::.*?Mins", '', text) # Remove video information
            
        else: 
            vid_length = '0'
            
        if 'href' in text:
            l = re.findall(r"\/\/([^\"]+)\">", text) # extract all URLs
            link = re.sub('[\'\[\]]', '', str(l)) # convert list to string
        else: 
            link = '0'
                         
        # remove all angle bracket contents
        text = re.sub(r"[\<].*?[\>]", '', text) 
        
        # ensure that all periods are followed by a space
        text = correct_spacing(text).strip()
        
        # remove all spaces between punctuation marks
        text = re.sub(r"(?<=[:.,!?()]) (?=[:.,!?()])", '', text)
        
        # Add one whitespace between one of [,:!?%] when it's followed by a letter
        text = re.sub(r"(?<=[,:!?%])(?=[A-Za-z])", ' ', text)
        
        #text = re.sub('"', '\\"', text)
        
        row = [productId, userId, profileName, help_num, help_den, score, \
               time, summary, text, link, vid_length]
        
        row = list(map(lambda x: x.rstrip('\n'), row))
        

        recordwriter.writerow(row)
            


                
