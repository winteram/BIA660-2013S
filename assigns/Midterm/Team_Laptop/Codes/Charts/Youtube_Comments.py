import re

data = file('comment_info_Dell.txt')
data2 = file('comment_info_HP.txt')

positive_total_dell = 0
negative_total_dell = 0
positive_total_hp = 0
negative_total_hp = 0

posfh = open('positive.txt', 'r')
positive_words = [line.strip() for line in posfh]
negfh = open('negative.txt', 'r')
negative_words = [line.strip() for line in negfh]

for line in data.readlines():
    positive_total_dell += len(re.findall('|'.join(positive_words), line))
    negative_total_dell += len(re.findall('|'.join(negative_words), line))
for line in data2.readlines():
    positive_total_hp += len(re.findall('|'.join(positive_words), line))
    negative_total_hp += len(re.findall('|'.join(negative_words), line))

import numpy as np
import matplotlib.pyplot as plt

dell = (positive_total_dell,negative_total_dell)
dellStd =(2, 3)

ind = np.arange(2)  # the x locations for the groups
width = 0.2       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, dell, width, color='r', yerr=dellStd)

hp = (positive_total_hp,negative_total_hp)
hpStd =   (2, 3)
rects2 = ax.bar(ind+width, hp, width, color='y', yerr=hpStd)
lenovo = (2639,363)
lvStd =(2,3)
rects3 = ax.bar(ind+2*width, lenovo, width, color='g', yerr=lvStd)
Apple = (100,17)
apStd =(2, 3)
rects4 = ax.bar(ind+3*width, Apple, width, color='b', yerr=apStd)
# add some
ax.set_ylabel('Times')
ax.set_title('Youtube Comments')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Positive', 'Negative') )

ax.legend( (rects1[0], rects2[0], rects3[0],rects4[0]), ('Dell', 'HP', 'Lenovo','Apple') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2, 1.01*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
plt.savefig("youtube_comment.png")
plt.show()

