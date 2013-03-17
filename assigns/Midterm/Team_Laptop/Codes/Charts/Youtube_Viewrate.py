import re
import numpy as np
import matplotlib.pyplot as plt
import csv

vwlen = 0
vwApp = 0
vwHP = 0
vwDel = 0
x = np.arange(4)
num1 = 0

f=open('Attention Rate of Youtube.csv','rU')
reader1=csv.reader(f)
for row in reader1:
    if(num1==1):
        vwlen = int(row[2])
    if(num1==2):
        vwApp = int(row[2])
    if(num1==3):
        vwHP = int(row[2])
    if(num1==4):
        vwDel = int(row[2])
    num1 = num1 + 1

viewrate = (vwDel,vwHP,vwlen,vwApp)
ax = plt.subplot(111)
plt.xlabel('Series')
plt.ylabel('View Rate')
plt.xticks( x + 0.4,  ('Dell','HP','Lenovo','Apple'))
rects1=plt.bar(x, viewrate, color='g')
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/1.5, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')
autolabel(rects1)
plt.savefig("View_rate.png")
plt.show()
f.close()

