# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:25:47 2013

@author: Tank
"""

import re
from string import punctuation

#begin clean-up of tweets
def cleanseTweet(tweet):
        #Convert to lower case
        tweet = tweet.lower()
        #Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',tweet)
        #replace @username to white space
        tweet = re.sub('@[^\s]+','',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+',' ', tweet)
        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #remove punctuation
        for p in list(punctuation):
            tweet=tweet.replace(p,'') 
        #to show only alpha\numeric characters
        tweet = re.sub('[^A-Za-z]+', ' ',tweet)
        #trim
        tweet = tweet.strip()
        return tweet 
        
