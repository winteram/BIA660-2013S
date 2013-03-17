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
f=open('tweets_Lenovo_05_01_50.csv','rU')
reader=csv.reader(f)
for row in reader:
    line_num = line_num + 1

figure(1, figsize=(6,6))
ax = axes([0.1,0.1, 0.8, 0.8])

labels = 'Negative','Positive','Nutural'
pos=int(row[5])
neg=int(row[4])
noc=int(row[0])-pos-neg

fracs = [neg,pos,noc]
explode=(0.05, 0.1, 0)
colors = ['blue', 'yellow', 'grey', 'red', 'green']  
pie(fracs, colors=colors, explode=explode, labels=labels, autopct='%1.4f%%', shadow=True)
title('Comments for Lenovo', bbox={'facecolor':'1', 'pad':5})
plt.savefig("Lenovo_comments.png")
plt.show()
num1 = 0
x = np.arange(3)
width = 0.35
for row in reader:
    if(num1==0):
        plt.xticks( x + width,  (row[1],row[2],row[3]) )
    num1 = num1 + 1
number = [int(row[1]),int(row[2]),int(row[3])]
ax = plt.subplot(111)
plt.xlabel('Series')
plt.ylabel('Attention Rate')
rects1=plt.bar(x, number, color='yellow')

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/1.5, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
plt.savefig("Lenovo_prod.png")
plt.show()
f.close()
