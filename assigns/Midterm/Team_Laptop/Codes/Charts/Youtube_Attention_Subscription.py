import re
import numpy as np
import matplotlib.pyplot as plt
import csv

sublen = 0
vwlen = 0
subApp = 0
vwApp = 0
subHP = 0
vwHP = 0
subDel = 0
vwDel = 0
num1 = 0

f=open('Attention Rate of Youtube.csv','rU')
reader1=csv.reader(f)
for row in reader1:
    if(num1==1):
        sublen = int(row[1])
        vwlen = int(row[2])
    if(num1==2):
        subApp = int(row[1])
        vwApp = int(row[2])
    if(num1==3):
        subHP = int(row[1])
        vwHP = int(row[2])
    if(num1==4):
        subDel = int(row[1])
        vwDel = int(row[2])
    num1 = num1 + 1

subscribe = (subDel,subHP,sublen,subApp)
subStd =(2, 3, 4, 2)

ind = np.arange(4)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, subscribe, width, color='y', yerr=subStd)

viewrate = (vwDel,vwHP,vwlen,vwApp)
vwStd =   (3, 5, 3, 4)
rects2 = ax.bar(ind+width, viewrate, width, color='b', yerr=vwStd)

# add some
ax.set_ylabel('Rate')
ax.set_title('Attention Rate from Youtube')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Dell', 'HP', 'Lenovo', 'Apple') )

ax.legend( (rects1[0], rects2[0]), ('Subscribe', 'Viewrate') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.savefig("Attention_youtube.png")
plt.show()

x = np.arange(4)
ax = plt.subplot(111)
plt.xlabel('Series')
plt.ylabel('Subscription Rate')
plt.xticks( x + 0.4,  ('Dell','HP','Lenovo','Apple'))
rects1=plt.bar(x, subscribe, color='b')
def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/1.5, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel2(rects1)
plt.savefig("Subscription_rate.png")
plt.show()
