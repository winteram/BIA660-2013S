#code for figure1
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
import re
import xlrd
import nltk

company_positive=[]
company_negative=[]
# creat a sheet and Excel table
bk=xlrd.open_workbook("table1.xlsx")   
sh = bk.sheet_by_name("Sheet1")
nrows = sh.nrows
ncols = sh.ncols
for i in range(2,5):
	cell_value= sh.cell_value(13,i)
	company_positive.append(cell_value)
for i in range(2,5):
	cell_value= sh.cell_value(14,i)
	company_negative.append(cell_value)

N = 3
#company_positive = (starbucks, Costa,DunkinDonuts)


company_positiveStd =   (2, 3, 4)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars


plt.subplot(111)
rects1 = plt.bar(ind, company_positive, width,
                    color='r',
                    yerr=company_positiveStd,
                    error_kw=dict(elinewidth=6, ecolor='pink'))
company_negativeStd =   (3, 5, 2)
rects2 = plt.bar(ind+width, company_negative, width,
                    color='y',
                    yerr=company_negativeStd,
                    error_kw=dict(elinewidth=6, ecolor='yellow'))
plt.ylabel('# Tweets')
plt.title('Starbucks and competitors')
plt.xticks(ind+width, ('Starbucks', 'Dunkin Donuts', 'Costa') )

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
#the code for figure2
company_positive_percentage = []
# creat a sheet and Excel table
bk=xlrd.open_workbook("table1.xlsx")   
sh = bk.sheet_by_name("Sheet1")
nrows = sh.nrows
ncols = sh.ncols
for i in range(2,5):
	cell_value = sh.cell_value(17,i)
	company_positive_percentage.append(cell_value)
 
#starbucks and competitors(positive/total
N = 3
ind = np.arange(N)
width = 0.35
company_positive_percentageStd =   (2, 3, 4)
rects3 = plt.bar(ind+width/2., company_positive_percentage, width,
                    color='r',
                    yerr=company_positive_percentageStd,
                    error_kw=dict(elinewidth=6, ecolor='pink'))
plt.ylabel('# Positive percentage')
plt.yticks(np.arange(0,101,10))
plt.title('Starbucks and competitors')
plt.xticks(ind+width, ('Starbucks', 'Dunkin Donuts', 'Costa') )



def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel2(rects3)
plt.show()
#the code for figure3
company_positive = []
company_negative = []
# creat a sheet and Excel table
bk=xlrd.open_workbook("table1.xlsx")   
sh = bk.sheet_by_name("Sheet1")
nrows = sh.nrows
ncols = sh.ncols
for i in range(1,8):
	cell_value = sh.cell_value(21,i)
	company_positive.append(cell_value)
for i in range(1,8):
	cell_value = sh.cell_value(22,i)
	company_negative.append(cell_value)
 
	
 
#starbucks and competitors (Positive and negative)
N = 7
################tweets positive about each coffee of starbucks
################
#company_positiveStd =   (1, 1, 1, 1, 1, 1, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars


plt.subplot(111)
rects1 = plt.bar(ind, company_positive, width,
                    color='r',
                    error_kw=dict(elinewidth=6, ecolor='pink'))
################tweets negative about each coffee of starbucks
################
#company_negativeStd =   (0, 0, 0, 0, 0, 0, 0)
rects2 = plt.bar(ind+width, company_negative, width,
                    color='y',
                    error_kw=dict(elinewidth=6, ecolor='yellow'))

# add some
plt.ylabel('# Tweets')
plt.title('Starbucks products')
plt.xticks(ind+width, ('Macchiato', 'Latte', 'Frappuccino', 'Mocha', 'Espresso', 'Skinny', 'Americano') )

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
#end

#the code for figure4
fracs = []
# creat a sheet and Excel table
bk=xlrd.open_workbook("table1.xlsx")   
sh = bk.sheet_by_name("Sheet1")
nrows = sh.nrows
ncols = sh.ncols
for i in range(2,5):
	cell_value= sh.cell_value(9,i)
	fracs.append(cell_value)

 
	#PieChart_latte
# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Starbucks', 'dunkin donuts', 'Costa'
################percentage of Starbucks, dunkin donuts, Costa (for latte)
################
explode=(0.05, 0, 0)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True)
title('Coffee Latte', bbox={'facecolor':'0.8', 'pad':5})
show()
#PieChart ends

#PieChart_CafeMocha
# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Starbucks', 'dunkin donuts', 'Costa'
################percentage of Starbucks, dunkin donuts, Costa (for CafeMocha )
fracs1 = []

for j in range(2,5):
	cell_value= sh.cell_value(10,j)
	fracs1.append(cell_value)
################
explode=(0.05, 0, 0)

pie(fracs1, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True)
title('CafeMocha', bbox={'facecolor':'0.8', 'pad':5})
show()
#PieChart ends


