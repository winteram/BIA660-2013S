import re
import numpy as np
import matplotlib.pyplot as plt
import csv

totlen = 0
totApp = 0
totHP = 0
totDel = 0
num1 = 0

f=open('data.csv','rU')
reader1=csv.reader(f)
for row in reader1:
    if(num1==1):
        totlen = int(row[3])
    if(num1==2):
        totApp = int(row[3])
    if(num1==3):
        totHP = int(row[3])
    if(num1==4):
        totDel = int(row[3])
    num1 = num1 + 1

total = (totDel,totHP,totlen,totApp)
totStd =(2, 3, 4, 2)

ind = np.arange(4)  # the x locations for the groups
width = 0.4      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind+width, total, width, color='y', yerr=totStd)
# add some
ax.set_ylabel('Times')
ax.set_title('Youtube Total Vedio')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Dell', 'HP', 'Lenovo', 'Apple') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/1.5, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
plt.savefig("Total_youtube.png")
plt.show()

