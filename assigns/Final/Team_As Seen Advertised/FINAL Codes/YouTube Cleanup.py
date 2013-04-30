# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:10:59 2013

@author: Tank
"""

import re
from string import punctuation

#begin clean-up of YouTube comments (YTC)
def cleanseYTC(YTC):
        #Convert to lower case
        YTC = YTC.lower()
        #Convert www.* or https?://* to URL
        YTC = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',YTC)
        #replace @username to white space
        YTC = re.sub('@[^\s]+','',YTC)
        #Remove additional white spaces
        YTC = re.sub('[\s]+',' ', YTC)
        #Replace #word with word
        YTC = re.sub(r'#([^\s]+)', r'\1', YTC)
        #remove punctuation
        for p in list(punctuation):
            YTC = YTC.replace(p,'') 
        #to show only alpha\numeric characters
        YTC = re.sub('[^A-Za-z]+', ' ',YTC)
        #trim
        YTC = YTC.strip()
        return YTC 
        
#Read the YTC's one by one and process it
fileObj = open('C:\\Users\\Tank\\Documents\\School\\FINAL660\\python_code\\youtubecommentsClean.txt',"w")

fp = open('C:\\Users\\Tank\\Documents\\School\\FINAL660\\python_code\\youtubecomments.txt', 'r')
line = fp.readline()
 
while line:
    ValidatedYTC = cleanseYTC(line)
    fileObj.write(ValidatedYTC+'\n')
    print ValidatedYTC
    line = fp.readline()
#end loop
fp.close()
fileObj.close()
