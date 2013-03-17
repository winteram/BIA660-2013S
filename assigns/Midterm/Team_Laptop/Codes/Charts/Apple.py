import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import numpy as np
import json
import pandas as pd
import time
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pylab import *

line_num = 0
f=open('tweets_Apple_04_20_20.csv','rU')
reader=csv.reader(f)
for row in reader:
    line_num = line_num + 1

figure(1, figsize=(6,6))
ax = axes([0.1,0.1, 0.8, 0.8])

labels = 'Negative','Positive'
pos=int(row[4])
neg=int(row[3])

fracs = [neg,pos]
explode=(0, 0.05)
colors = ['grey','yellow','blue', 'red', 'green']  
pie(fracs, colors=colors, explode=explode, labels=labels, autopct='%1.4f%%', shadow=True)
title('Comments for Apple', bbox={'facecolor':'1', 'pad':5})
plt.savefig("Apple_comments.png")
plt.show()
num1 = 0
x = np.arange(2)
for row in reader:
    if(num1==0):
        plt.xticks( x + 0.4,  (row[1],row[2]))
    num1 = num1 + 1
    
number = [int(row[1]),int(row[2])]
ax = plt.subplot(111)
plt.xlabel('Series')
plt.ylabel('Attention Rate')
rects1=plt.bar(x, number, color='orange')
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/1.5, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
plt.savefig("Apple_prod.png")
plt.show()
f.close()
