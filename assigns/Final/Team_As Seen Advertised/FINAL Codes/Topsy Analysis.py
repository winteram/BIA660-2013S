import urllib2
import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
from pylab import *
import twitter
import re
import tweepy
import cleaning_validating_algorithm as cl
from bs4 import BeautifulSoup
import urllib
import xlwt
import csv
from time import sleep;
from string import punctuation

def query(term1,term2,page):
    ValidatedTweet = ''
    a =''
    for i in range (1,page):
        search = urllib2.urlopen("http://topsy.com/s/"+term1+"+"+term2+"/tweet?allow_lang=en&window=m&om=b&offset="+str(i*10)+"&page="+str(i))
        html = search.read()
        soup = BeautifulSoup(html)
        for body in soup.findAll('div',class_="twitter-post-big"):#The body loop
            for tweet in body.findAll('span',{"class":"twitter-post-text translatable language-en"}):#The tweets loop
                a = tweet.text.encode("utf-8")
                myfile.write(a +'\n')
                ValidatedTweet=cl.cleanseTweet(a)
                tweets.append(ValidatedTweet)
                print ValidatedTweet,'\n'
                
  
def sentAna():
    worktable = xlwt.Workbook(encoding='utf-8')
    sheet = worktable.add_sheet("sheet1")
    # open the Positvie an Negative list
    posfh = open('posi.txt','r')
    negfh = open('neg.txt','r')
    count_neg = 0
    count_pos = 0
    #The list of result 
    index =[]
    positive_words = [word.strip() for word in posfh ] 
    negative_words = [word.strip() for word in negfh ]
    for line in tweets:
        count_pos = 0
        count_neg = 0
        a = line.split(' ')
        for i in a:
            if (i in positive_words):
                count_pos = count_pos +1
            if (i in negative_words):
                count_neg = count_neg +1

        ratio = (float(count_pos)-float(count_neg))/len(a)
        index.append((float(count_pos)-float(count_neg))/len(a))
        #print float(len(set(a)))/float(len(a))
     
    for i in range(1,len(index)):
        sheet.write(i-1,0,tweets[i-1])
        sheet.write(i-1,1,index[i-1])
    worktable.save("result2")
    Positive_Tweets = 0 
    Negative_Tweets = 0
    Neutral_Tweets = 0
    for ind in index:
        if (ind>0):
            Positive_Tweets +=1      
        if (ind<0):
            Negative_Tweets +=1      
        if(ind==0):
            Neutral_Tweets +=1
    Positive_Com.append(Positive_Tweets)
    Negative_Com.append(Negative_Tweets)

    print "The Number of Positive Tweets = ",Positive_Tweets,'\n'
    print "The Number of Negative Tweets = ", Negative_Tweets,'\n'
    print "The Number of Neutral Tweets = " ,Neutral_Tweets,'\n'
    print "The total tweets = ", len(index)





if __name__ == "__main__":
    Positive_Com = []
    Negative_Com = []
    tweets  = []
    myfile = open("get.txt","a")
#ran 5 advertisements at once two times to capture tweets
    query("will+it+blend", "",100)# The first argument is the keyword we want to search, and the second argument is the number of pages you need. 
    sentAna()
    tweets  = []
    query("oldspice","",100)
    sentAna()
    tweets  = []
    query("evian","",100)
    sentAna()
    tweets  = []
    query("microsoft","",100)
    sentAna()
    tweets  = []
    query("etrade","",100)
    sentAna()
    tweets  = []
    myfile.close()
    print "Finished"



