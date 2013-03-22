#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amir
#
# Created:     04/03/2013
# Copyright:   (c) Amir 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


print "loading packages ..."
import twitter
import numpy as np
import json
import pandas as pd
import time
from collections import Counter
import en
print "loading is done!"

#Login in twitter

starttime = time.strftime("%d_%H_%M",time.localtime())

print"Twitter Authentication ..."

api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')
print api.VerifyCredentials().name
print"Authentication is done"


print "Pulling data from twitter"

Term='galaxy S3'
fname="Database/tweets_"+Term+'_'+starttime+".csv"

tweets=[]

tweets=api.GetSearch(term=Term, geocode=None, since_id=None, per_page=1, page=1, lang='en', show_user='true', query_users=False)
maxID=tweets[0].id

N=1 # number of iterations
NPage=15 # Number of pages (Maximum=15)

L=0 #Accumulative Number of tweets
f=open(fname,'w')
tweets=[]
for j in range(N):
    print "Number of iteration = ", j

    for i in range(1,NPage):
#Searching tweets
            newTweets=api.GetSearch(term=Term, geocode=None, since_id=None, per_page=100, page=i, lang='en', show_user='true', query_users=False)
            print"Page Number = ", i, " , Tweets per Page = ", tweets.__len__()
            L+=newTweets.__len__()


#saving the data base as json
            print"Saving..."
            for t in newTweets:
                    tweet = json.loads(str(t))
                    tweets.append(tweet)
#		print tweet




            twitterData = pd.DataFrame(tweets)
            twitterData.to_csv(fname,encoding="utf-8")
            maxID=t.id # Setting to the last ID of the tweets




            print"Successful Saving!"


    print"Waiting ....."
    time.sleep(1)

f.close()
print"Accumulative Number of tweets = ", L

print "Data collectiong is done!"
