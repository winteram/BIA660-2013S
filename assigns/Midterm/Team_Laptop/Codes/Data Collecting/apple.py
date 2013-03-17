'''
Created on Mar 2, 2013

@author: Allen
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import numpy as np
import json
import pandas as pd
import time
import re

consumer_key="HrI9pkJWwsdTL1jv9fDmg"
consumer_secret="xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI"
access_token="19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA"
access_token_secret="bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A"

positive_total = 0
negative_total = 0
macbook = 0
macair = 0

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream. 
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self):
        self.tweets = []
        self.starttime = time.strftime("%d_%H_%M",time.localtime())

    def on_data(self, data):
        global positive_total, negative_total, macbook, macair
        
        posfh = open('positive.txt', 'r')
        positive_words = [line.strip() for line in posfh]
        negfh = open('negative.txt', 'r')
        negative_words = [line.strip() for line in negfh]
               
        tweet = json.loads(data)

        tweet_dict = {}
        try:
            tweet_dict['text'] = tweet['text']
        except KeyError:
            return True
        try:   
            tweet_dict['time'] = tweet['created_at']
        except KeyError:
            return True
        
        if(len(re.findall('|'.join(positive_words), tweet['text'])) != 0 & len(re.findall('|'.join(negative_words), tweet['text'])) == 0):
            positive_total += 1
        if(len(re.findall('|'.join(positive_words), tweet['text'])) == 0 & len(re.findall('|'.join(negative_words), tweet['text'])) != 0):
            negative_total += 1

        
        macbook_list = ['Macbook', 'macbook', 'MacBook']
        macair_list = ['macair','Macair', 'MacBook']
                
        macbook += len(re.findall('|'.join(macbook_list), tweet['text']))
        macair += len(re.findall('|'.join(macair_list), tweet['text']))
       
        tweet_dict['positive_total'] = positive_total
        tweet_dict['negative_total'] = negative_total
        tweet_dict['Macbook'] = macbook
        tweet_dict['Macair'] = macair
      
#        print tweet
        self.tweets.append(tweet_dict)
        if len(self.tweets) % 30 == 0:
            print len(self.tweets)
            twitterData = pd.DataFrame(self.tweets)
            twitterData.to_csv("tweets_Apple_"+self.starttime+".csv",encoding="utf-8")
        if len(self.tweets) > 20000:
            exit(0)
        else:
            return True

    def on_error(self, status):
        print 'error' + status

    def on_timeout(self):        
        print "timeout!"
        return False


lis = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, lis, timeout = 60)    
stream.filter(track=['macbook','macair'])
