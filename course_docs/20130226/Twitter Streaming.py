# do pip install tweepy first
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import numpy as np
import json
import pandas as pd
import time

consumer_key="HrI9pkJWwsdTL1jv9fDmg"
consumer_secret="xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI"
access_token="19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA"
access_token_secret="bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A"


class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def __init__(self):
		self.tweets = []
		self.starttime = time.strftime("%d_%H_%M",time.localtime())

	def on_data(self, data):
		tweet = json.loads(data)
#		print tweet
		self.tweets.append(tweet)
		if len(self.tweets) % 30 == 0:
			print len(self.tweets)
			twitterData = pd.DataFrame(self.tweets)
			twitterData.to_csv("tweets_"+self.starttime+".csv",encoding="utf-8")
		if len(self.tweets) > 200:
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

stream = Stream(auth, lis, timeout=60)	
stream.filter(track=['song'])


