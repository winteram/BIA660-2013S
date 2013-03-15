'''

	BIA 660 Mid-term Project

	Team:

		Team-RIM
	
	Members:

		Han Yan: hyan2@stevens.edu
		Minhui Gu: mgu1@stevens.edu
		Sen Yang: syang12@stevens.edu
		Aruna: acheruvu@stevens.edu
		Priyanka: pkalangu@stevens.edu

	Created by Han Yan
	
'''

import re
from collections import defaultdict
from collections import Counter

file_list = ['data_Android_comments.txt', 'data_bb_comments.txt', 'data_blackberry10_comments.txt', 'data_ios_comments.txt', 'data_iPhone_comments.txt', 'data_JellyBean_comments.txt', 'data_WindowsPhone_comments.txt', 'data_wp8_comments.txt']
hottest_dict = {'app' : 0, 'apps' : 0, 'OS' : 0, 'software' : 0, 'hardware' : 0, 'ecosystem' : 0, 'screen' : 0, 'experience' : 0, 'UI' : 0, 'battery' : 0}
manufacturer_dict = {'HTC' : 0, 'Samsung' : 0, 'Nokia' : 0, 'RIM' : 0, 'Apple' : 0, 'Google' : 0, 'Microsoft' : 0}

# Target files
with open('twitter_result_wp8_5000.txt') as f:
    commentsFile = f.read().splitlines()

# Key word dictionary
with open('positive.txt') as f:
    positive_list = f.read().splitlines()

# Key word dictionary
with open('negative.txt') as f:
    negative_list = f.read().splitlines()

# Key word dictionary
with open('mentioned_others_for_wp_keywords.txt') as f:
    others = f.read().splitlines()

count_dict = defaultdict(int)

# Count the frenquency of the keywords
def count_data(type, count):
    global count_dict
    count_dict[type] += count

# Seach words from each file and count the frequency of those words
def count_to_dict(cFile, keywordList):
	for line in cFile:
		for i in range(0, len(keywordList)):
			pattern_p = re.compile(keywordList[i])
			count_data(keywordList[i], len(re.findall(pattern_p, line)))

def countComments(cDict):
	return sum(cDict.values())

def countWordFromfile(filename):

	f=open(filename,'r')

	wordcount=0

	for lines in f:

		f1=lines.split()

		wordcount=wordcount+len(f1)

	f.close()
	return wordcount

# Find the hottest words in each files
def topRankedWords(filename, frequency):
	f = open(filename, 'r')
	hottest = []
	words_gen = f.read()

	top_words = Counter((words_gen).split(' ')).most_common()

	for word, frequency in top_words:
		if (frequency > 500):
			hottest.append((word, frequency))
	f.close()
	return hottest

# Calculate the total number of the hottest words
def countHottestWords(fileNameList, wordsDict):
	for i in fileNameList:
		for j in topRankedWords(i, 100):
			for k in wordsDict.keys():
				if k in j:
					wordsDict[k] += j[1]


# count_to_dict(commentsFile, negative_list)
# print count_dict
# countHottestWords(file_list, hottest_dict)
# countHottestWords(file_list, manufacturer_dict)
# print hottest_dict
# print manufacturer_dict


# DATA (theverge.com)
bb10_positive = {'beautiful': 26, 'fantastic': 37, 'love': 204, 'awesome': 87, 'satisfied': 7, 'comfortable': 7, 'thankful': 6, 'curious': 30, 'best': 246, 'encouraged': 2, 'nice': 225, 'deserve': 18, 'fast': 164, 'appreciative': 0, 'amazing': 67, 'wonderful': 8, 'easy': 112, 'lovely': 2, 'friendly': 10, 'happy': 45, 'good': 725, 'joy': 46, 'safe': 21, 'interested': 66, 'cool': 100, 'great': 384, 'like': 2032, 'fulfilled': 0, 'rock': 32, 'loving': 7, 'amazed': 6}
bb10_negative = {'uninterested': 0, 'restless': 0, 'garbage': 15, 'tired': 24, 'exhausted': 1, 'nothing': 190, 'uncomfortable': 4, 'fail': 203, 'miserable': 2, 'indifferent': 1, 'hate': 217, 'withdrawn': 1, 'slow': 72, 'overwhelmed': 1, 'delay': 41, 'f\\*\\**': 4, 'horrible': 38, 'disappoint': 30, 'dislike': 13, 'smell': 5, 'worse': 64, 'unprofessional': 0, 'agitated': 0, 'worst': 32, 'numb': 235, 'terrified': 0, 'awful': 32, 'disappointed': 13, 'not like': 24, 'cry': 30, 'upset': 6, 'terrible': 57, 'stressed out': 0, 'bad': 260, 'horrified': 1, 'f\\*\\*k': 1}

jellybean_positive = {'beautiful': 41, 'fantastic': 39, 'love': 319, 'awesome': 154, 'satisfied': 9, 'comfortable': 26, 'thankful': 3, 'curious': 26, 'best': 372, 'encouraged': 0, 'nice': 256, 'deserve': 31, 'fast': 314, 'appreciative': 0, 'amazing': 110, 'wonderful': 16, 'easy': 148, 'lovely': 11, 'friendly': 14, 'happy': 103, 'good': 722, 'joy': 64, 'safe': 23, 'interested': 55, 'cool': 107, 'great': 525, 'like': 2259, 'fulfilled': 2, 'rock': 57, 'loving': 11, 'amazed': 7}
jellybean_pnegative = {'uninterested': 1, 'restless': 0, 'garbage': 16, 'tired': 23, 'exhausted': 0, 'nothing': 211, 'uncomfortable': 6, 'fail': 115, 'miserable': 1, 'indifferent': 0, 'hate': 252, 'withdrawn': 1, 'slow': 168, 'overwhelmed': 0, 'delay': 80, 'f\\*\\**': 3, 'horrible': 46, 'disappoint': 68, 'dislike': 9, 'smell': 9, 'worse': 105, 'unprofessional': 0, 'agitated': 0, 'worst': 54, 'numb': 272, 'terrified': 0, 'awful': 38, 'disappointed': 31, 'not like': 43, 'cry': 36, 'upset': 18, 'terrible': 70, 'stressed out': 1, 'bad': 270, 'horrified': 0, 'f\\*\\*k': 1}

wp8_positive = {'beautiful': 108, 'fantastic': 65, 'love': 426, 'awesome': 163, 'satisfied': 15, 'comfortable': 20, 'thankful': 3, 'curious': 46, 'best': 480, 'encouraged': 2, 'nice': 390, 'deserve': 61, 'fast': 246, 'appreciative': 0, 'amazing': 140, 'wonderful': 16, 'easy': 167, 'lovely': 6, 'friendly': 22, 'happy': 160, 'good': 1180, 'joy': 117, 'safe': 48, 'interested': 93, 'cool': 176, 'great': 640, 'like': 3545, 'fulfilled': 3, 'rock': 44, 'loving': 14, 'amazed': 12}
wp8_negative = {'uninterested': 1, 'restless': 0, 'garbage': 56, 'tired': 43, 'exhausted': 0, 'nothing': 379, 'uncomfortable': 2, 'fail': 216, 'miserable': 4, 'indifferent': 2, 'hate': 411, 'withdrawn': 0, 'slow': 144, 'overwhelmed': 1, 'delay': 68, 'f\\*\\**': 21, 'horrible': 64, 'disappoint': 100, 'dislike': 31, 'smell': 11, 'worse': 124, 'unprofessional': 0, 'agitated': 3, 'worst': 66, 'numb': 345, 'terrified': 2, 'awful': 46, 'disappointed': 47, 'not like': 63, 'cry': 67, 'upset': 37, 'terrible': 91, 'stressed out': 0, 'bad': 467, 'horrified': 1, 'f\\*\\*k': 3}

ios6_positive = {'beautiful': 81, 'fantastic': 47, 'love': 391, 'awesome': 160, 'satisfied': 15, 'comfortable': 30, 'thankful': 6, 'curious': 42, 'best': 671, 'encouraged': 5, 'nice': 333, 'deserve': 80, 'fast': 366, 'appreciative': 1, 'amazing': 164, 'wonderful': 16, 'easy': 115, 'lovely': 7, 'friendly': 28, 'happy': 199, 'good': 1207, 'joy': 110, 'safe': 54, 'interested': 77, 'cool': 146, 'great': 762, 'like': 3284, 'fulfilled': 2, 'rock': 45, 'loving': 19, 'amazed': 11}
ios6_negative = {'uninterested': 0, 'restless': 0, 'garbage': 34, 'tired': 40, 'exhausted': 0, 'nothing': 359, 'uncomfortable': 10, 'fail': 256, 'miserable': 6, 'indifferent': 0, 'hate': 435, 'withdrawn': 0, 'slow': 228, 'overwhelmed': 2, 'delay': 42, 'f\\*\\**': 8, 'horrible': 81, 'disappoint': 100, 'dislike': 25, 'smell': 13, 'worse': 226, 'unprofessional': 2, 'agitated': 0, 'worst': 57, 'numb': 324, 'terrified': 2, 'awful': 62, 'disappointed': 49, 'not like': 77, 'cry': 37, 'upset': 39, 'terrible': 126, 'stressed out': 0, 'bad': 559, 'horrified': 1, 'f\\*\\*k': 0}

glass_positive = {'beautiful': 62, 'fantastic': 38, 'love': 389, 'awesome': 245, 'satisfied': 3, 'comfortable': 39, 'thankful': 3, 'curious': 42, 'best': 416, 'encouraged': 3, 'nice': 274, 'deserve': 37, 'fast': 286, 'appreciative': 0, 'amazing': 201, 'wonderful': 25, 'easy': 114, 'lovely': 14, 'friendly': 24, 'happy': 100, 'good': 818, 'joy': 110, 'safe': 64, 'interested': 100, 'cool': 344, 'great': 565, 'like': 3083, 'fulfilled': 5, 'rock': 44, 'loving': 6, 'amazed': 9}
glass_negative = {'uninterested': 2, 'restless': 0, 'garbage': 15, 'tired': 24, 'exhausted': 0, 'uncomfortable': 16, 'fail': 193, 'miserable': 3, 'indifferent': 0, 'hate': 327, 'withdrawn': 0, 'slow': 117, 'overwhelmed': 1, 'delay': 27, 'f\\*\\**': 8, 'horrible': 37, 'disappoint': 72, 'dislike': 14, 'smell': 13, 'worse': 93, 'unprofessional': 2, 'agitated': 0, 'worst': 32, 'numb': 201, 'terrified': 1, 'awful': 41, 'disappointed': 39, 'not like': 62, 'cry': 47, 'upset': 20, 'terrible': 86, 'stressed out': 0, 'bad': 298, 'horrified': 1, 'f\\*\\*k': 2}

# DATA (twitter)
t_bb10_positive = {'beautiful': 30, 'fantastic': 1, 'love': 403, 'awesome': 24, 'satisfied': 1, 'comfortable': 1, 'thankful': 0, 'curious': 1, 'best': 100, 'encouraged': 0, 'nice': 30, 'deserve': 1, 'fast': 26, 'appreciative': 0, 'amazing': 11, 'wonderful': 4, 'easy': 13, 'lovely': 2, 'friendly': 7, 'happy': 45, 'good': 86, 'joy': 46, 'safe': 7, 'interested': 8, 'cool': 166, 'great': 34, 'like': 216, 'fulfilled': 1, 'rock': 34, 'loving': 16, 'amazed': 0}
t_bb10_negative = {'uninterested': 0, 'restless': 0, 'garbage': 7, 'tired': 2, 'exhausted': 0, 'uncomfortable': 0, 'fail': 19, 'miserable': 2, 'indifferent': 0, 'hate': 103, 'withdrawn': 0, 'slow': 13, 'overwhelmed': 1, 'delay': 1, 'f\\*\\**': 2, 'horrible': 0, 'disappoint': 2, 'dislike': 0, 'smell': 1, 'worse': 10, 'unprofessional': 0, 'agitated': 0, 'worst': 19, 'numb': 20, 'terrified': 0, 'awful': 7, 'disappointed': 0, 'not like': 1, 'cry': 24, 'upset': 0, 'terrible': 2, 'stressed out': 0, 'bad': 175, 'horrified': 0, 'f\\*\\*k': 1}
t_android_positive = {'beautiful': 7, 'fantastic': 0, 'love': 136, 'awesome': 167, 'satisfied': 1, 'comfortable': 0, 'thankful': 0, 'curious': 0, 'best': 30, 'encouraged': 0, 'nice': 7, 'deserve': 1, 'fast': 9, 'appreciative': 0, 'amazing': 41, 'wonderful': 18, 'easy': 15, 'lovely': 3, 'friendly': 8, 'happy': 10, 'good': 27, 'joy': 41, 'safe': 1, 'interested': 3, 'cool': 25, 'great': 46, 'like': 59, 'fulfilled': 0, 'rock': 29, 'loving': 1, 'amazed': 1}
t_android_negative = {'uninterested': 0, 'restless': 0, 'garbage': 0, 'tired': 1, 'exhausted': 0, 'uncomfortable': 0, 'fail': 4, 'miserable': 0, 'indifferent': 0, 'hate': 19, 'withdrawn': 0, 'slow': 6, 'overwhelmed': 0, 'delay': 0, 'f\\*\\**': 0, 'horrible': 2, 'disappoint': 0, 'dislike': 1, 'smell': 0, 'worse': 1, 'unprofessional': 0, 'agitated': 0, 'worst': 1, 'numb': 6, 'terrified': 0, 'awful': 1, 'disappointed': 0, 'not like': 1, 'cry': 0, 'upset': 0, 'terrible': 2, 'stressed out': 0, 'bad': 57, 'horrified': 0, 'f\\*\\*k': 0}
t_ios_positive = {'beautiful': 43, 'fantastic': 2, 'love': 509, 'awesome': 89, 'satisfied': 0, 'comfortable': 1, 'thankful': 1, 'curious': 2, 'best': 107, 'encouraged': 0, 'nice': 38, 'deserve': 8, 'fast': 71, 'appreciative': 0, 'amazing': 28, 'wonderful': 5, 'easy': 13, 'lovely': 5, 'friendly': 5, 'happy': 52, 'good': 66, 'joy': 49, 'safe': 10, 'interested': 52, 'cool': 49, 'great': 65, 'like': 228, 'fulfilled': 0, 'rock': 27, 'loving': 12, 'amazed': 0}
t_ios_negative = {'uninterested': 0, 'restless': 0, 'garbage': 0, 'tired': 6, 'exhausted': 1, 'uncomfortable': 0, 'fail': 13, 'miserable': 1, 'indifferent': 0, 'hate': 52, 'withdrawn': 0, 'slow': 17, 'overwhelmed': 0, 'delay': 0, 'f\\*\\**': 4, 'horrible': 4, 'disappoint': 0, 'dislike': 2, 'smell': 3, 'worse': 6, 'unprofessional': 0, 'agitated': 0, 'worst': 5, 'numb': 27, 'terrified': 0, 'awful': 1, 'disappointed': 0, 'not like': 2, 'cry': 18, 'upset': 0, 'terrible': 5, 'stressed out': 0, 'bad': 221, 'horrified': 0, 'f\\*\\*k': 0}
t_wp8_positive = {'beautiful': 12, 'fantastic': 1, 'love': 271, 'awesome': 19, 'satisfied': 0, 'comfortable': 1, 'thankful': 1, 'curious': 3, 'best': 80, 'encouraged': 0, 'nice': 19, 'deserve': 7, 'fast': 13, 'appreciative': 0, 'amazing': 23, 'wonderful': 5, 'easy': 7, 'lovely': 0, 'friendly': 3, 'happy': 25, 'good': 89, 'joy': 16, 'safe': 2, 'interested': 6, 'cool': 46, 'great': 32, 'like': 152, 'fulfilled': 0, 'rock': 81, 'loving': 10, 'amazed': 4}
t_wp8_negative = {'uninterested': 0, 'restless': 0, 'garbage': 2, 'tired': 4, 'exhausted': 1, 'uncomfortable': 0, 'fail': 5, 'miserable': 1, 'indifferent': 0, 'hate': 30, 'withdrawn': 0, 'slow': 7, 'overwhelmed': 0, 'delay': 0, 'f\\*\\**': 3, 'horrible': 0, 'disappoint': 2, 'dislike': 0, 'smell': 1, 'worse': 1, 'unprofessional': 0, 'agitated': 0, 'worst': 8, 'numb': 7, 'terrified': 0, 'awful': 2, 'disappointed': 1, 'not like': 1, 'cry': 11, 'upset': 1, 'terrible': 1, 'stressed out': 0, 'bad': 167, 'horrified': 0, 'f\\*\\*k': 0}

# print countComments(t_wp8_positive)
# print countComments(t_wp8_negative)
print countWordFromfile('twitter_BB_5000.txt') + countWordFromfile('twitter_result_Android.txt') + countWordFromfile('twitter_result_iOS.txt') + countWordFromfile('twitter_result_wp8_5000.txt')
print (countWordFromfile('user.txt') - countWordFromfile('per.txt'))
# Positive / Negative words counting.
# from theverge.com
bb10 = [('positive', 4722), ('negative', 1617)]
jellybean = [('positive', 5824), ('negative', 1948)]
wp8 = [('positive', 8408), ('negative', 2916)]
ios6 = [('positive', 8474), ('negative', 3200)]
google_glass = [('positive', 7463), ('negative', 1794)]

# from twitter
t_bb10 = [('positive', 1314), ('negative', 412)]
t_jellybean = [('positive', 686), ('negative', 102)]
t_ios = [('positive', 1537), ('negative', 388)]
t_wp8 = [('positive', 928), ('negative', 256)]

# Count mentioned others
ios_mentioned_others = {'Microsoft': 372, 'Google': 4635, 'WP8': 132, 'Nexus 7': 212, 'Jellybean': 22, 'Windows Surface': 0, 'windows phone': 35, 'blackberry 10': 0, 'RIM': 29, 'Nexus 10': 13, 'blackberry': 19, 'wp8': 28, 'Android': 2092, 'BlackBerry 10': 5, 'android': 648, 'Windows Phone': 208, 'BlackBerry': 18}
bb10_mentioned_others = {'iPad': 90, 'Google': 322, 'WP8': 294, 'Apple': 516, 'Jellybean': 10, 'Nexus 7': 25, 'iOS': 790, 'windows phone': 129, 'ios': 86, 'Microsoft': 419, 'Nexus 10': 0, 'iPhone': 732, 'wp8': 42, 'Android': 1516, 'Windows Phone': 456, 'android': 495}
jellybean_mentioned_others = {'iPad': 702, 'RIM': 14, 'Microsoft': 156, 'WP8': 74, 'Apple': 1429, 'iOS': 1064, 'windows phone': 20, 'ios': 96, 'blackberry 10': 0, 'BlackBerry': 12, 'blackberry': 17, 'wp8': 6, 'BlackBerry 10': 3, 'Windows Phone': 96, 'iPhone': 757}
wp8_mentioned_others = {'iPad': 426, 'Google': 7010, 'Nexus 7': 64, 'Jellybean': 74, 'ios': 368, 'Apple': 2696, 'iOS': 2936, 'iPhone': 2782, 'blackberry 10': 6, 'RIM': 126, 'Nexus 10': 4, 'blackberry': 62, 'Android': 5190, 'BlackBerry 10': 6, 'android': 1264, 'BlackBerry': 48}

ios_mentioned_others = [('Windows Phone', 747), ('Android', 7622), ('BlackBerry', 71)]
bb10_mentioned_others = [('Windows Phone', 1340), ('Android', 2378), ('iOS', 2214)]
jellybean_mentioned_others = [('Windows Phone', 352), ('BlackBerry', 46), ('iOS', 4048)]
wp8_mentioned_others = [('Android', 13606), ('BlackBerry', 248), ('iOS', 9208)]

# Hottest words counter
hot_word = {'hardware': 3902, 'UI': 1784, 'ecosystem': 856, 'battery': 2198, 'OS': 7194, 'app': 15181, 'apps': 15266, 'screen': 6140, 'experience': 1736, 'software': 2516}
manuf_word = {'Google': 18751, 'HTC': 2119, 'Apple': 21376, 'Samsung': 5933, 'Nokia': 4748, 'RIM': 3852, 'Microsoft': 7939}

# a = sorted(hot_word.items(), key=lambda hot_word:hot_word[1])
# a.reverse() 
# b = sorted(manuf_word.items(), key=lambda manuf_word:manuf_word[1])
# b.reverse()
# print a
# print b