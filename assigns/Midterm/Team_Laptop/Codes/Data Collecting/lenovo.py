'''
Created on Mar 3, 2013

@author: Allen
'''
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

consumer_key="ZCTmRNa0UCsVGv5thPRrbw"
consumer_secret="76pSb01h4uB2dwwbhdnQbU3fqjzhNTPl2hjqaaSfQ"
access_token="1086456919-W6m7QQTPqYVXa8Mgs1xiFstGEhmoLXinYCLKgbp"
access_token_secret="JYFqabknNIaq2nAiPMmkHIianAYD5SzwJ2O5QjFNac"

positive_total = 0
negative_total = 0
thinkpad = 0
ideapad = 0
essential = 0

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream. 
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self):
        self.tweets = []
        self.starttime = time.strftime("%d_%H_%M",time.localtime())

    def on_data(self, data):
        global positive_total, negative_total, thinkpad, ideapad, essential
        
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
        
        thinkpad_list = ['ThinkPad T', 'ThinkPad X', 'ThinkPad L', 'thinkpad W', 'thinkpad T', 'thinkpad X', 'thinkpad L', 'thinkpad W']
        ideapad_list = ['IdeaPad Y','IdeaPad Yoga', 'IdeaPad u', 'IdeaPad S', 'IdeaPad Z', 'ideapad Y','ideapad Yoga', 'ideapad u', 'ideapad S', 'ideapad Z']
        essential_list = ['Essential', 'Essential G', 'essential', 'essential G']
                
        thinkpad += len(re.findall('|'.join(thinkpad_list), tweet['text']))
        ideapad += len(re.findall('|'.join(ideapad_list), tweet['text']))
        essential += len(re.findall('|'.join(essential_list), tweet['text']))
       
        tweet_dict['positive_total'] = positive_total
        tweet_dict['negative_total'] = negative_total
        tweet_dict['ThinkPad'] = thinkpad
        tweet_dict['IdeaPad'] = ideapad
        tweet_dict['Essential'] = essential
      
#        print tweet
        self.tweets.append(tweet_dict)
        if len(self.tweets) % 2 == 0:
            print len(self.tweets)
            twitterData = pd.DataFrame(self.tweets)
            twitterData.to_csv("tweets_"+self.starttime+".csv",encoding="utf-8")
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
stream.filter(track=['lenovo','thinkpad','ideapad'])
