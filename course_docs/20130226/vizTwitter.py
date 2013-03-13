import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
from pylab import *
import twitter
import re

# create interface for Twitter API
api = twitter.Api(consumer_secret='yUp8DLewT0S88wOwqrDw',consumer_key='ReoGMpdkmdwuLR6hIVep1pk98Nye3Xb0XP4joPVoOY',access_token_key='1228573202-iZrLcTVmvuQ7aZbm4xtIqdgzcQQ2XZ9BlwCFtog',access_token_secret='a4U4T3hxD7VLJCNdlM4dZWxcWUUy7AD7IvonNQnk6o')

# List of keywords
keywds = ['flight','airline','usair','united','delta','jetblue']

posfh = open('goodFlight.txt','r')
positive_words = [line for line in posfh]
negfh = open('badFlight.txt','r')
negative_words = [line for line in posfh]

d = []
for keyword in keywds:
	someTweets = api.GetSearch(keyword)
	for tweet in someTweets:
	    if 'text' in tweet:
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
			tweet_dict['location'] = tweet.user.location
			# num followers
			tweet_dict['followers'] = tweet.user.followers_count
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

# factor that indicates which airline is most mentioned
df['airline'] = 

# num mentions of each airline
airline_counts = 

# num mentions of each airline per keyword

# bar chart
ind = np.arange(4)  # the x locations for the groups
width = 0.35       # the width of the bars
rects = plt.bar(ind, airline_counts, width, color='r')
# labels
plt.ylabel('# Tweets')
plt.xticks(ind+width, ('US', 'UA', 'DL', 'JB') )
# show plot
plt.show()


# box-plot of characters per tweet
plt.figure()
plt.boxplot(df['nchars'],0,'gD')
plt.show()

# histogram of num words per tweet
avgwds = np.mean(df['nwords'])
sdwds = np.std(df['nwords'])

# the histogram of the data
n, bins, patches = plt.hist(df['nwords'], 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, avgwds, sdwds)
l = plt.plot(bins, y, 'r--', linewidth=2)

plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.title('Histogram of Words Per Tweet')

minplot = min(df['nwords']) - np.ceil(0.1*(max(df['nwords']) - min(df['nwords'])))
maxplot = max(df['nwords']) + np.ceil(0.1*(max(df['nwords']) - min(df['nwords'])))
plt.axis([minplot, maxplot, 0, max(n)])
plt.grid(True)

plt.show()


# num positive words
# num negative words

# t-test
sm.CompareMeans(df['positive'],df['negative'])
stats.ttest_ind(df['positive'],df['negative'])

# average positive tweets for each airline
avg_pos = 
sd_pos =
# average negative tweets for each airline
avg_neg = 
sd_neg =


# bar chart of positive & negative
plt.subplot(111)
rects1 = plt.bar(ind, avg_pos, width,
                    color='g',
                    yerr=sd_pos,
                    error_kw=dict(elinewidth=2, ecolor='black'))
rects2 = plt.bar(ind+width, avg_neg, width,
                    color='r',
                    yerr=sd_neg,
                    error_kw=dict(elinewidth=2, ecolor='black'))
# labels
plt.ylabel('Avg mentions')
plt.title('Positive and Negative Airline Mentions')
plt.xticks(ind+width, ('US', 'UA', 'DL', 'JB') )

plt.legend( (rects1[0], rects2[0]), ('Positive', 'Negative') )
plt.show()

# regression
res = sm.OLS(df['positive'],df['negative']).fit()
res.summary()

# scatterplot of pos & neg
plt.scatter(df['positive'],df['negative'],c=df['airline'])
plt.line(res.params[])
