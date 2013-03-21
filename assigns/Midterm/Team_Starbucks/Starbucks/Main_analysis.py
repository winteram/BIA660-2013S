import urllib2
import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
from pylab import *
import matplotlib.pyplot as plt
import twitter
import re
from twitter import Api
import tweepy
import cleaning_validating_algorithm as cl
from bs4 import BeautifulSoup
import urllib
import xlwt
import csv
from time import sleep;
from string import punctuation

# this program may take 15 minuts because it need crawl a website to get data
# you can set the number of page in the function, if you set it small, it will spend less
#time to run, but you get few data.
def query(term1,term2,page):
    ValidatedTweet = ''
    a =''
    for i in range (1,page):
        search = urllib2.urlopen("http://topsy.com/s/"+term1+"+"+term2+"/tweet?allow_lang=en&window=m&om=b&offset="+str(i*10)+"&page="+str(i))
        html = search.read()
        soup = BeautifulSoup(html)
        for body in soup.findAll('div',class_="twitter-post-big"):#The body loop
            for tweet in body.findAll('span',{"class":"twitter-post-text translatable language-en"}):#The tweets loop
                a = tweet.text
                myfile.write(a.encode("utf-8")+'\n')
                print a,'\n'
                ValidatedTweet=cl.cleanseTweet(a)
                tweets.append(tweet.text)
   

def sentAna():
    worktable = xlwt.Workbook(encoding='utf-8')
    sheet = worktable.add_sheet("sheet1")
    # open the Positvie an Negative list
    posfh = open("posi.txt",'r')
    negfh = open("nega.txt",'r')
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
    Natural_Tweets = 0
    for ind in index:
        if (ind>0):
            Positive_Tweets +=1      
        if (ind<0):
            Negative_Tweets +=1      
        if(ind==0):
            Natural_Tweets +=1
    Positive_Com.append(Positive_Tweets)
    Negative_Com.append(Negative_Tweets)

    print "The Number of Positive Tweets = ",Positive_Tweets,'\n'
    print "The Number of Negative Tweets = ", Negative_Tweets,'\n'
    print "The Number of Natural Tweets = " ,Natural_Tweets,'\n'
    print "The total tweets = ", len(index)


# the main function
if __name__ == "__main__":
    Positive_Com = []
    Negative_Com = []
    tweets  = []
    page = input ("Please input the number of page you want : ")
    myfile = open("get.txt","a")
    query("Starbucks","",page)# The first argument is the keyword we want to search, and the second argument is the number of pages you need. 
    sentAna()
    tweets  = []
    query("Costa","Coffee",page)
    sentAna()
    tweets  = []
    query("Dunkin","Donuts",page)
    sentAna()
    tweets  = []
    myfile.close()
    print "Finished"
# this part is for chart 
    
N = 3
#company_positive = (starbucks, Costa,DunkinDonuts)
company_positive = (Positive_Com[0], Positive_Com[1], Positive_Com[2])

company_positiveStd =   (2, 3, 4)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars


plt.subplot(111)
rects1 = plt.bar(ind, company_positive, width,
                    color='r',
                    yerr=company_positiveStd,
                    error_kw=dict(elinewidth=6, ecolor='pink'))
company_negative = (Negative_Com[0], Negative_Com[1], Negative_Com[2])
company_negativeStd =   (3, 5, 2)
rects2 = plt.bar(ind+width, company_negative, width,
                    color='y',
                    yerr=company_negativeStd,
                    error_kw=dict(elinewidth=6, ecolor='yellow'))
plt.ylabel('# Tweets')
plt.title('Starbucks and competitors')
plt.xticks(ind+width, ('Starbucks', 'Costa', 'Dunkin Donuts') )

plt.legend( (rects1[0], rects2[0]), ('Positive', 'Negative') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()





