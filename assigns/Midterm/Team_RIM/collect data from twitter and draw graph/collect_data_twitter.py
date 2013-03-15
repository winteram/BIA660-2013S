''' collect data from twitter stream'''

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import simplejson
import time
import sys

consumer_key="7wnCr6sWPiLuwS9dQorw"
consumer_secret="NUFQVzuJlq85hbSZBtojSP0ZYCemRHCJGPar6Dm0"
access_token="813616172-jJUHjITBDH5R6JMtQDyWhNuklpg7gh3ExOxk7dfU"
access_token_secret="soW2G8dS66QIXyrsg6Ia9vHOgydUs7ngjJBjJqendM"

TWITTER_NUMBER = 1000
d=[]
dict = {}
TRACKWHAT = []
	
class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	use TWITTER_NUMBER to control the tweet number.
	data will be writen into a txt file
	"""
	def __init__(self, api = None, fprefix = 'streamer'):
		self.counter = 0
		
	def on_data(self, data):
		self.counter +=1
		tweet_dict = {}
		print self.counter
		dict = simplejson.loads(data)
	 	d = simplejson.dumps(dict, sort_keys = False, indent = 4)
		file = open(TRACKWHAT[0]+".txt", 'a')
		file.write(d)
		if self.counter >=TWITTER_NUMBER:
			self.counter = 0
			stream.disconnect()
			print "connect closed"
		
	def on_error(self, status):
		print status


if __name__ == '__main__':
	TRACKWHAT.append(sys.argv[1])
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	# record the time to calculate the tweet per second in the end
	file = open(TRACKWHAT[0]+".txt", 'w')
	file.write(time.strftime('%H:%M:%S',time.localtime(time.time())))
	stream.filter(track=TRACKWHAT)
	file = open(TRACKWHAT[0]+".txt", 'a')
	file.write(time.strftime('%H:%M:%S',time.localtime(time.time())))
