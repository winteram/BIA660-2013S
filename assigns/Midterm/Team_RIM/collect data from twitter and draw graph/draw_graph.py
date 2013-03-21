''' draw different graphs'''

import time
import re
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import datetime
import statsmodels.api as sm
from pygooglechart import PieChart3D
from matplotlib.colors import colorConverter


def dateDiffInSeconds(date1, date2):
	timedelta = date2 - date1
	return timedelta.days*24*3600 + timedelta.seconds
	
def draw_pie(what,thetitle):
	fig = plt.figure(1, figsize=(6,6))
	ax = fig.add_subplot(111)
	ax.axis('equal')
	colors=('b', 'r', 'g', 'w', 'm', 'burlywood', 'c', 'y')
	title(thetitle)
	ax.pie([value for (key, value) in what],colors=colors ,labels=[key for (key, value) in what], autopct='%1.1f%%')
	plt.show()
	
def draw_columns(what):
	ind = np.arange(len(what)) #set x axi number
	width = 0.5
	rects = plt.bar(ind, [value for (key, value) in what], width, color='y')
	autolabel(rects)
	plt.ylabel('#words')
	plt.xticks(ind+(width/2),[key for (key, value) in what])
	plt.show()
	
def	draw_line_graph(what,xlable,ylable):
	plt.figure
	plt.xticks(range(len(what)),[key for (key, value) in what])
	y_series = [value for (key, value) in what]
	plt.plot(y_series)
	plt.xlabel(xlable)
	plt.ylabel(ylable)
	plt.show()
	
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

if __name__ == '__main__':

	#data
	ios_per_month_comments = [('201203', 90), ('201204', 94), ('201205', 579), ('201206', 3987), ('201207', 108), ('201208', 1476), ('201209', 8409), ('201210', 3379), ('201211', 436), ('201212', 1569), ('201301', 432), ('201302', 432)]
	bb10_per_month_comments = [('201203', 36), ('201204', 104), ('201205', 1262), ('201206', 543), ('201207', 645), ('201208', 203), ('201209', 1080), ('201210', 75), ('201211', 604), ('201212', 779), ('201301', 3396), ('201302', 497)]
	jellybean_per_month_comments = [('201112', 380), ('201202', 148), ('201203', 380), ('201206', 4039), ('201207', 2905), ('201208', 2204), ('201209', 613), ('201210', 2409), ('201211', 1033), ('201212', 173), ('201301', 217), ('201302', 93)]
	wp8_per_month_comments = [('201202', 366), ('201204', 1009), ('201206', 2959), ('201207', 933), ('201208', 1888), ('201209', 2640), ('201210', 2980), ('201211', 1908), ('201212', 1939), ('201301', 3149), ('201302', 224), ('201303', 18)]	
	iphone_per_month_comments = [('201110', 929), ('201203', 167), ('201204', 468), ('201206', 969), ('201207', 3157), ('201208', 2402), ('201209', 13116), ('201210', 112), ('201211', 1173), ('201212', 2421), ('201301', 1524), ('201302', 2207)]
	blackberry_per_month_comments = [('201202', 1006), ('201204', 160), ('201205', 721), ('201206', 328), ('201208', 72), ('201209', 979), ('201210', 418), ('201211', 323), ('201212', 1211), ('201301', 4706), ('201302', 937), ('201303', 197)]
	android_per_month_comments = [('201203', 357), ('201204', 307), ('201205', 209), ('201206', 2802), ('201207', 2937), ('201208', 931), ('201209', 1492), ('201210', 2909), ('201211', 2316), ('201212', 1145), ('201301', 1188), ('201302', 3437)]
	windowsphone_per_month_comments = [('201203', 990), ('201204', 1861), ('201206', 2328), ('201207', 565), ('201208', 1638), ('201209', 2013), ('201210', 4067), ('201211', 1447), ('201212', 2576), ('201301', 4625), ('201302', 1189), ('201303', 301)]
	ios_mentioned_others = [('Windows Phone', 747), ('Android', 7622), ('BlackBerry', 71)]
	bb10_mentioned_others = [('Windows Phone', 1340), ('Android', 2378), ('iOS', 2214)]
	jellybean_mentioned_others = [('Windows Phone', 352), ('BlackBerry', 46), ('iOS', 4048)]
	wp8_mentioned_others = [('Android', 13606), ('BlackBerry', 248), ('iOS', 9208)]
	hottest_words = [('apps', 15266), ('OS', 7194), ('screen', 6140), ('hardware', 3902), ('battery', 2198), ('UI', 1784), ('experience', 1736), ('ecosystem', 856)]
	hottest_manufacturer = [('Apple', 21376), ('Google', 18751), ('Microsoft', 7939), ('Samsung', 5933), ('Nokia', 4748), ('RIM', 3852), ('HTC', 2119)]	
	comments = [('twitter.com', 20000), ('theverge.com', 151475)]
	words = [('twitter.com', 2800000), ('theverge.com', 8390112)]
	sum_of_comments_specific_topics = [('Blackberry 10', 9890), ('iOS 6', 20991), ('Android Jellybean', 14872), ('Windows Phone 8', 20013)]
	sum_of_comments_general_topics = [('Blackberry', 11856),('iPhone', 28645),  ('Android', 20805), ('Windows Phone', 24358)]
	bb10 = [('positive words', 4722), ('negative words', 1617)]
	jellybean = [('positive words', 5824), ('negative words', 1948)]
	wp8 = [('positive words', 8408), ('negative words', 2916)]
	ios6 = [('positive words', 8474), ('negative words', 3200)]	
	google_glass = [('positive', 7463), ('negative', 1794)]
	
	# ****** pie chart		
	draw_pie(sum_of_comments_general_topics,'General')

	
	#***** tweet per second column graph	
	date1 = datetime.datetime(2013,03,04,16,30,46)
	date2 = datetime.datetime(2013,03,04,16,39,38)
	dateDiffInSeconds(date1,date2)
	t_ios =  532   #calculate same way as above
	t_android = 487
	t_bb = 2192
	t_wp8 = 17515
	
	time_android = 5000/t_android
	time_ios = 5000/t_ios
	time_BB = 5000/t_bb
	time_wp = 5000/t_wp8
	tweet_per_second = [('android',time_android),('ios',time_ios),('blackberry',time_BB),('windows phone',time_wp)]

    # *******column graph
	draw_columns(comments)
	
	#******total comment graph
	comment_total = [('the_verge',151475),('twitter_streaming',20000)]	
	t_bb10 = [('positive', 1314), ('negative', 412)]
	t_jellybean = [('positive', 686), ('negative', 102)]
	t_ios = [('positive', 1537), ('negative', 388)]
	t_wp8 = [('positive', 928), ('negative', 256)]
	fig = plt.figure(1, figsize=(6,6))
	ax = fig.add_subplot(111)
	ax.axis('equal')
	title('tweets mentioning iOS')
	colors=( 'g','r','y','w','b','m','burlywood','c')
	ax.pie([value for (key, value) in t_ios],colors=colors ,labels=['positive:\n1537','negative:\n388'], autopct='%1.1f%%')
	plt.show()

	#*********line graph	
	
	# draw_line_graph(iphone_per_month_comments,'iOS','comments')
	# draw_line_graph(blackberry_per_month_comments,'BlackBerry','comments')
	# draw_line_graph(android_per_month_comments,'Android','comments')
	draw_line_graph(windowsphone_per_month_comments,'Windows Phone','comments')
	
	#******multi-column graph		
	bb10 = [('positive words', 4722), ('negative words', 1617)]
	jellybean = [('positive words', 5824), ('negative words', 1948)]
	wp8 = [('positive words', 8408), ('negative words', 2916)]
	ios6 = [('positive words', 8474), ('negative words', 3200)]	

	ind = np.arange(2)  # the x locations for the groups
	width = 0.15       # the width of the bars	
	plt.subplot(111)
	rects1 = plt.bar(ind, [value for (key, value) in bb10], width,color='r')
	rects2 = plt.bar(ind+width,[value for (key, value) in jellybean], width,color='y')
	rects3 = plt.bar(ind+2*width,[value for (key, value) in wp8], width,color='g')
	rects4 = plt.bar(ind+3*width,[value for (key, value) in ios6], width,color='b')
	rects5 = plt.bar(ind+4*width,[value for (key, value) in google_glass], width,color='w')
	plt.ylabel('comments')
	plt.xticks(ind+2*width, [key for (key, value) in bb10])
	plt.legend( (rects1[0], rects2[0],rects3[0], rects4[0]), ('BlackBerry 10', 'Android Jellybean','Windows Phone 8','iOS 6') )	
	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)	
	plt.show()

