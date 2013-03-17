import re
import numpy as np
import matplotlib.pyplot as plt
import csv

toplen = 0
topApp = 0
topHP = 0
topDel = 0
toplen1 = 0
topApp1 = 0
topHP1 = 0
topDel1 = 0
num1 = 0

f=open('data.csv','rU')
reader1=csv.reader(f)
for row in reader1:
    if(num1==1):
        toplen1 = int(row[4])
        toplen = int(row[5])
    if(num1==2):
        topApp1 = int(row[4])
        topApp = int(row[5])
    if(num1==3):
        topHP1 = int(row[4])
        topHP = int(row[5])
    if(num1==4):
        topDel1 = int(row[4])
        topDel = int(row[5])
    num1 = num1 + 1

top = (topDel,topHP,toplen,topApp)
totStd =(2, 3, 4, 2)

ind = np.arange(4)  # the x locations for the groups
width = 0.4      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind+width, top, width, color='y', yerr=totStd)
# add some
ax.set_ylabel('Times')
ax.set_title('Top 10 Youtube total view count for Each Company ')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Dell', 'HP', 'Lenovo', 'Apple') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/1.5, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
plt.savefig("Top10_view_youtube.png")
plt.show()

top1 = (topDel1,topHP1,toplen1,topApp1)
totStd =(2, 3, 4, 2)
ind = np.arange(4)  # the x locations for the groups
width = 0.4      # the width of the bars
rects2 = ax.bar(ind+width, top1, width, color='y', yerr=totStd)
# add some
ax.set_ylabel('Times')
ax.set_title('Top 10 Youtube total comment for Each Company ')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Dell', 'HP', 'Lenovo', 'Apple') )
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/1.5, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects2)
plt.savefig("Top10_youtube.png")
plt.show()

