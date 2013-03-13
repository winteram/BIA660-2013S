# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
from pylab import *
import matplotlib.pyplot as plt
import twitter
import re

# <codecell>

api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')

# <codecell>

keywds = ['flight','airline','usair','united','delta','jetblue']

# <codecell>

posfh = open('goodFlight.txt','r')
positive_words = [line.strip() for line in posfh]
negfh = open('badFlight.txt','r')
negative_words = [line.strip() for line in negfh]

# <codecell>

negative_words

# <codecell>

positive_words

# <codecell>

d = []
for keyword in keywds:
	someTweets = api.GetSearch(keyword, per_page=200)
	for tweet in someTweets:
		tweet_dict = {}
		# keyword
		tweet_dict['keyword'] = keyword
		# user
		tweet_dict['user'] = tweet.user.screen_name
		# text
		tweet_dict['text'] = tweet.text
		# num words
		tweet_dict['nwords'] = len(tweet.text.split(' '))
		# num chars
		tweet_dict['nchars'] = len(tweet.text)
		# location
		#tweet_dict['location'] = tweet.user.location
		# num followers
		#tweet_dict['followers'] = tweet.user.followers_count
		# num usair mentions
		tweet_dict['usair'] = len(re.findall('usair',tweet.text))
		# num united mentions
		tweet_dict['united'] = len(re.findall('united',tweet.text))
		# num delta mentions
		tweet_dict['delta'] = len(re.findall('delta',tweet.text))
		# num jetblue mentions
		tweet_dict['jetblue'] = len(re.findall('jetblue',tweet.text))
		# num positive words
		tweet_dict['positive'] = len(re.findall('|'.join(positive_words),tweet.text))
		# num negative words
		tweet_dict['negative'] = len(re.findall('|'.join(negative_words),tweet.text))
		d.append(tweet_dict)
df = pd.DataFrame(d)

# <codecell>

df[:2]

# <codecell>

df.text[0]

# <codecell>

df.user[:2]

# <codecell>

df2 = df[['delta','usair','united','jetblue']]

# <codecell>

df2[:2]

# <codecell>

df2 = df2.where(df2>0)

# <codecell>

df2[:5]

# <codecell>

df['airline_max'] = max(df2)

# <codecell>

df[:2]

# <codecell>

airline_counts = df2.sum()
airline_counts

# <codecell>

stats.chisquare(airline_counts)

# <codecell>

ind = np.arange(4)  # the x locations for the groups
width = 0.75       # the width of the bars
plt.bar(ind, airline_counts, width, color='b')
# labels
plt.ylabel('# Tweets')
plt.xticks(ind+(width/2), ('DL', 'UA', 'UN', 'JB') )
# show plot
plt.show()

# <codecell>

print df.nchars.median()
print df['nchars'].max()
print df.nchars.min()

# <codecell>

plt.figure()
plt.boxplot(df['nchars'],0,'gD')
plt.ylabel("Number of characters")
plt.show()

# <codecell>

avgwds = df.nchars.mean()
sdwds = df.nchars.std()

# <codecell>

n, bins, patches = plt.hist(df['nchars'], 20, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, avgwds, sdwds)
l = plt.plot(bins, y, 'r-', linewidth=2)

plt.xlabel('Number of Characters')
plt.ylabel('Frequency')
plt.title('Histogram of Words Per Tweet')

minplot = min(df['nchars']) - np.ceil(0.1*(max(df['nchars']) - min(df['nchars'])))
maxplot = max(df['nchars']) + np.ceil(0.1*(max(df['nchars']) - min(df['nchars'])))
plt.axis([min(df.nchars), max(df.nchars), 0, max(n)+0.01])
plt.grid(True)

plt.show()

# <codecell>

res = sm.OLS(df['nchars'],df['nwords']).fit()
res.summary()

# <codecell>

m,b = polyfit(df['nwords'], df['nchars'], 1) 

plot(df['nwords'], df['nchars'], 'yo', df['nwords'], m*df['nwords']+b, '--k') 
show()

# <codecell>

df['airlinetotal'] = df['jetblue'] + df['united'] + df['usair'] + df['delta']

# <codecell>

df3 = df[df.airlinetotal>0]

# <codecell>

df3.text.count()

# <codecell>

df3[:5]

# <codecell>

print df3.positive.sum()
print df3.negative.sum()

# <codecell>

stats.ttest_ind(df[df.keyword=="united"].nchars,df[df.keyword=="usair"].nchars)

# <codecell>

df[df.keyword=="united"].nchars.mean()

# <codecell>

df[df.keyword=="usair"].nchars.mean()

# <codecell>

155 / 7

# <codecell>

tweetd = []
someTweets = api.GetSearch("airline", per_page=100, page=1)
for tweet in someTweets:
    tweetd.append(tweet.text)

# <codecell>

len(tweetd)

# <codecell>

someTweets = api.GetSearch("airline", per_page=100, page=2)
for tweet in someTweets:
    tweetd.append(tweet.text)

# <codecell>

tweetd[:2]

# <codecell>

tweetd[102:108]

# <codecell>

re.findall('(?<!not )like','i do not like this sam i am')

# <codecell>

test = u'\u2134'

# <codecell>

test.encode('utf-8')

# <codecell>

from twitter import Api

# <codecell>

import tweepy

# <codecell>


