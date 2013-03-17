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
insprion = 0
xps = 0
allenware = 0
latitude = 0


class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream. 
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self):
        self.tweets = []
        self.starttime = time.strftime("%d_%H_%M",time.localtime())

    def on_data(self, data):
        global positive_total, negative_total, insprion, xps, allenware, latitude
        
        posfh = open('positive.txt', 'r')
        positive_words = [line.strip() for line in posfh]
        negfh = open('negative.txt', 'r')
        negative_words = [line.strip() for line in negfh]
               
        tweet = json.loads(data)

        tweet_dict = {}
        try:
            tweet_dict['text_content'] = tweet['text']
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
        
        insprion_list = ['Insprion', 'insprion']
        xps_list = ['XPS','xps']
        allenware_list = ['Allenware','allenware']
        latitude_list = ['Latitude', 'latitude']
        
        insprion += len(re.findall('|'.join(insprion_list), tweet['text']))
        xps += len(re.findall('|'.join(xps_list), tweet['text']))
        allenware += len(re.findall('|'.join(allenware_list), tweet['text']))
        latitude += len(re.findall('|'.join(latitude_list), tweet['text']))
        
        tweet_dict['positive_total'] = positive_total
        tweet_dict['negative_total'] = negative_total
        tweet_dict['Insprion'] = insprion
        tweet_dict['XPS'] = xps
        tweet_dict['Allenware'] = allenware
        tweet_dict['Latitude'] = latitude
        
#        print tweet
        self.tweets.append(tweet_dict)
        if len(self.tweets) % 30 == 0:
            print len(self.tweets)
            twitterData = pd.DataFrame(self.tweets)
            twitterData.to_csv("tweets_DELL_"+self.starttime+".csv",encoding="utf-8")
        if len(self.tweets) > 20000:
            exit(0)
        else:
            return True

    def on_error(self, status):
        print status

    def on_timeout(self):        
        print "timeout!"
        return False


lis = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, lis, timeout = 60)    
stream.filter(track=['dell', 'xps', 'insprion', 'allenware', 'dell latitude'])
