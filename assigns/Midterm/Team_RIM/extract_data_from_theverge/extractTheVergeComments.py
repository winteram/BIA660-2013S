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

'''

import urllib2
import simplejson
import json
import unicodedata
from BeautifulSoup import BeautifulSoup
import re
import datetime

def printData(urlList):
	for item in urlList:
		print item

# Compate data time
def compareDate(dStr1, dstr2):
	dlist1 = dStr1.split("-")
	dlist2 = dstr2.split("-")
	dTime1 = datetime.date(int(dlist1[0]), int(dlist1[1]), int(dlist1[2]))
	dTime2 = datetime.date(int(dlist2[0]), int(dlist2[1]), int(dlist2[2]))
	if (dTime1 < dTime2):
		return False
	else:
		return True

# Sort urlList by date time
def sortUrl(urlList):
	for i in range(0, len(urlList)):
		for j in range(i+1, len(urlList)):
			if compareDate(urlList[i]['date'], urlList[j]['date']):
				urlList[i], urlList[j] = urlList[j], urlList[i]


def countComments(list):
	num = 0
	for i in list:
		try:
			num += int(i['commentsNum'])
		except KeyError:
			continue
	return num

# Read each element from result data structure and save it to a list. Structure example: [ {}, {}, {}, ... ]
def saveEachToList(list):
	newList = []
	for i in list:
		for j in i:
			newList.append(j)
	return newList

# Make search result data structure. Structure example: [ [ {}, {}, ...], [{}, {}, ...], [{}, {}, ... ] ]
def buildUrlList(urlJson):
	result = []
	for items in urlJson['items']:
		dict = {}
		if (items['pagemap']['metatags'][0].has_key('sailthru.date')):
			dict['title'] = items['title']
			dict['date'] = items['pagemap']['metatags'][0]['sailthru.date']
			dict['url'] = items['pagemap']['metatags'][0]['og:url']
			result.append(dict)
	return result

# Build Commonts dictionary sorted by date
def buildCommentsList(urlList):
	list = []
	for item in urlList:
		dict = {}
		dict['date'] = item['date']
		try:
			dict['num'] = int(item['commentsNum'])
		except KeyError:
			dict['num'] = 0
		list.append(dict)
	return list

# Get related content(json) from google's search service using its REST search api and save the content into a list.
# Each content is a dictionary with the key url, date and title
def searchGoogle(QUERY):
	gResult = []
	BASE ="https://www.googleapis.com/customsearch/v1?"
	KEY = "AIzaSyD3Y8LKhuxHj2cLplPuXAEMxutCDba0iQM"
	CX = "007508388893477587358:vbpmj68-dgg"
	# QUERY = "windows+phone"
	SITE = "www.theverge.com"
	FORMAT = "json"

	for i in range(0,10):
		page = "page" + str(i+1)
		count = "%d"%(i*10+1)
		restUrl = BASE+"key="+KEY+"&cx="+CX+"&q="+QUERY+"&start="+count+"&alt="+FORMAT+"&siteSearch="+SITE
		search = urllib2.urlopen(restUrl)
		# s = simplejson.loads(search.read())
		# print simplejson.dumps(s, sort_keys = False, indent = 4)
		gResult.append(buildUrlList(simplejson.loads(search.read())))

	return gResult

# Find comments ID from each page in theverge.com and use this id as a request to get comments data from theverge's comments database
def findId(url):
	pattern = re.compile("Chorus.Comments.entry_id*")
	source = urllib2.urlopen(url)
	soup = BeautifulSoup(source.read())
	scriptTagContent = soup.findAll('script', text=re.compile("Chorus.Comments.entry_id*"), limit = 1)
	try:
		gotdata = scriptTagContent[0]
	except IndexError:
		return 0
	return re.findall('(?<=Chorus\.Comments\.entry_id = )[0-9]+',scriptTagContent[0].string).pop()

# Get the number of each page's comments
def findCommentNumberAndID(urlList):
	for item in urlList:
		cmtsID = findId(item['url'])
		source = urllib2.urlopen(item['url'])
		soup = BeautifulSoup(source.read())
		result = soup.findAll('span',{'class':'comment-count big'})
		num = re.findall('<span class="update-with-count">(.*?)</span>', str(result))
		item['commentsID'] = cmtsID
		if (num != []):
			item['commentsNum'] = int(num.pop())
	
# print all of the comments from each page
def extractCommentbyID(commentsId, fileName):
	f = open(fileName, 'a')
	if (commentsId != 0):
		search = urllib2.urlopen("http://www.theverge.com/comments/load_comments/" + commentsId)
	 	dict = simplejson.loads(search.read())
	 	#print simplejson.dumps(dict, sort_keys = False, indent = 4)
	 	for result in range (0, len(dict["comments"])):
	 		# print dict['comments'][result]['body'].encode('utf8')
	 		content = dict['comments'][result]['body'].encode('utf8')
	 		print >> f, content

# save all of comments to a txt file
def extractComments(urlList, fileName):
	for item in urlList:
		extractCommentbyID(item['commentsID'], fileName)

	# f = open(fileName, 'a')
	# list = []
	# for item in urlList:
	# 	list == extractCommentbyID(item['commentsID'], fileName)
	# 	for i in list:
	# 		print i
	# print >> f, list
	# f.close()




# The interface to get the search result.
# Search url information from google and use those url to extract comments from theverge.com with the comments number.
# Change the keyword to get different result.
def searchFromTheVerge(keyword):
	searchResult = saveEachToList(searchGoogle(keyword))
	findCommentNumberAndID(searchResult)
	return searchResult


def sumByMonth(cmlist):
	dict = {}
	for item in cmlist:
		dateList = item['date'].split("-")
		YearMonth = ''.join(dateList[0:2])
		if dict.has_key(YearMonth):
			try:
				dict[YearMonth] += item['num']
			except KeyError:
				dict[YearMonth] += 0
		else:
			try:
				dict[YearMonth] = item['num']
			except KeyError:
				dict[YearMonth] += 0
	return sorted(dict.items())

# def extractFromFile(fileName):
# 	f = open(fileName, 'r')
# 	soup = BeautifulSoup(f.read())
# 	print soup

# rGoogleGlass = [{'date': '2013-02-22', 'url': 'http://www.theverge.com/2013/2/22/4013406/i-used-google-glass-its-the-future-with-monthly-updates', 'commentsID': u'3777447', 'commentsNum': 1351, 'title': 'I used Google Glass: the future, but with monthly updates | The Verge'}, {'date': '2013-02-20', 'url': 'http://www.theverge.com/2013/2/20/4008180/google-glass-ui-previewed-in-new-video', 'commentsID': u'3772221', 'commentsNum': 648, 'title': 'New Google Glass UI video shows off search, camera, and voice ...'}, {'date': '2013-02-22', 'url': 'http://www.theverge.com/2013/2/22/4017634/google-glass-for-consumers-planned-to-ship-in-2013-and-cost-less-than-1500', 'commentsID': u'3781675', 'commentsNum': 136, 'title': 'Google aims to sell Glass to consumers this year for less than ...'}, {'date': '2013-02-22', 'url': 'http://www.theverge.com/2013/2/22/4017148/a-day-in-google-glass-video', 'commentsID': u'3781189', 'commentsNum': 12, 'title': 'Video: I used Google Glass | The Verge'}, {'date': '2013-01-31', 'url': 'http://www.theverge.com/2013/1/31/3938182/google-glass-revealed-in-fcc-filing', 'commentsID': u'3702223', 'commentsNum': 146, 'title': 'Google Glass headset with bone-conduction speakers revealed in ...'}, {'date': '2013-02-23', 'url': 'http://www.theverge.com/2013/2/22/4019596/google-glass-microsoft-new-xbox-hacking-attacks-90sotv', 'commentsID': u'3783637', 'commentsNum': 13, 'title': "90 Seconds on The Verge: Google Glass, Microsoft's new Xbox, and ..."}, {'date': '2013-01-01', 'url': 'http://www.theverge.com/2013/1/1/3825348/google-project-glass-work-in-progress', 'commentsID': u'3589389', 'commentsNum': 120, 'title': 'Google Glass lead says project is still a work in progress | The Verge'}, {'date': '2013-03-01', 'url': 'http://www.theverge.com/2013/3/1/4043476/jetblues-google-glass-enhanced-airport-mockups', 'commentsID': u'3807517', 'commentsNum': 5, 'title': "Gallery: JetBlue's Google Glass-enhanced airport mockups | The ..."}, {'date': '2013-02-20', 'url': 'http://www.theverge.com/2013/2/20/4006748/google-project-glass-explorer-edition-pre-order', 'commentsID': u'3770789', 'commentsNum': 100, 'title': "Google expands Glass pre-orders to 'creative individuals' - The Verge"}, {'date': '2013-02-27', 'url': 'http://www.theverge.com/2013/2/27/4035920/fake-google-glass-ebay-listing-bid-up-to-15900-before-being-pulled', 'commentsID': u'3799961', 'commentsNum': 18, 'title': 'Fake Google Glass eBay listing bid up to $15,900 before being ...'}, {'date': '2013-03-01', 'url': 'http://www.theverge.com/2013/3/1/4043372/jetblue-enters-google-glass-competition-with-airport-mockups', 'commentsID': u'3807413', 'commentsNum': 60, 'title': 'JetBlue mocks up its own vision of a Google Glass-enhanced airport ...'}, {'date': '2012-09-11', 'url': 'http://www.theverge.com/2012/9/11/3315542/google-glass-heads-up-display-voice-controls-functionality-details', 'commentsID': u'3079583', 'commentsNum': 132, 'title': 'Google Glass moves beyond photography: details on heads-up ...'}, {'date': '2012-06-27', 'url': 'http://www.theverge.com/2012/6/27/3121288/google-glass-explorer-edition-announcement', 'commentsID': u'2885329', 'commentsNum': 189, 'title': 'Google announces Google Glass Explorer Edition, $1,500 pre-order ...'}, {'date': '2013-03-01', 'url': 'http://www.theverge.com/2012/4/4/2925372/google-project-glass-augmented-reality', 'commentsID': 0, 'title': 'Google Glass heads up display: science fiction you can wear | The ...'}, {'date': '2013-02-24', 'url': 'http://www.theverge.com/2013/2/24/4021768/the-weekender-google-glass-chromebook-pixel-and-the-ps4-event', 'commentsID': u'3785809', 'commentsNum': 3, 'title': 'The Weekender: Google Glass, Chromebook Pixel, and the PS4 ...'}, {'date': '2013-02-20', 'url': 'http://www.theverge.com/2013/2/20/4008192/google-glass-press-pictures', 'commentsID': u'3772233', 'commentsNum': 0, 'title': 'Gallery: Google Glass press pictures | The Verge'}, {'date': '2013-02-21', 'url': 'http://www.theverge.com/2013/2/20/4011092/ps4-google-glass-90sotv', 'commentsID': u'3775133', 'commentsNum': 29, 'title': '90 Seconds on The Verge: PlayStation 4 and Google Glass | The ...'}, {'date': '2013-01-16', 'url': 'http://www.theverge.com/2013/1/15/3880972/google-hosting-project-glass-hackathons-in-san-francisco-and-new-york', 'commentsID': u'3645013', 'commentsNum': 58, 'title': 'Google hosting Project Glass hackathons in San Francisco and New ...'}, {'date': '2012-06-28', 'url': 'http://www.theverge.com/2012/6/28/3123287/sergey-brin-google-glass-consumer-launch-early-2014', 'commentsID': u'2887328', 'commentsNum': 56, 'title': 'Sergey Brin hopes to bring Google Glass to consumers by early ...'}, {'date': '2013-02-21', 'url': 'http://www.theverge.com/2013/2/20/4011964/google-glass-focuses-on-fashion-negotiating-with-warby-parker', 'commentsID': u'3776005', 'commentsNum': 54, 'title': 'Google focuses on fashion with Glass, reportedly talking ... - The Verge'}, {'date': '2013-02-27', 'url': 'http://www.theverge.com/2013/2/27/4036366/sergey-brin-at-ted-the-cell-phone-is-a-nervous-habit', 'commentsID': u'3800407', 'commentsNum': 291, 'title': "Sergey Brin on the touchscreen: 'it's kind of emasculating' | The Verge"}, {'date': '2012-06-27', 'url': 'http://www.theverge.com/2012/6/27/3121164/project-glass-demo-io', 'commentsID': u'2885205', 'commentsNum': 124, 'title': 'Google shows off Project Glass at I/O with live skydiving and bike ...'}, {'date': '2012-06-27', 'url': 'http://www.theverge.com/2012/6/27/3121858/googles-project-glass-first-impressions-with-sergey-brins-headset', 'commentsID': u'2885899', 'commentsNum': 181, 'title': "Google's Project Glass: first impressions (with Sergey Brin's headset ..."}, {'date': '2012-11-13', 'url': 'http://www.theverge.com/2012/11/13/3641414/vizux-m100-smart-glasses-sdk', 'commentsID': u'3405455', 'commentsNum': 108, 'title': 'Google Glass gets some competition from the Vuzix M100 smart ...'}, {'date': '2012-05-25', 'url': 'http://www.theverge.com/2012/5/25/3042684/google-project-glass-video-sample', 'commentsID': u'2806725', 'commentsNum': 135, 'title': "First video sample from Google's Project Glass | The Verge"}, {'date': '2012-04-04', 'url': 'http://www.theverge.com/2012/4/4/2925292/google-project-glass-contact-lenses', 'commentsID': u'2689333', 'commentsNum': 73, 'title': "Could Google's Project Glass be used in contact lenses? | The Verge"}, {'date': '2012-04-06', 'url': 'http://www.theverge.com/2012/4/6/2929927/google-project-glass-modeled-by-sergey-brin-first-high-res-photos', 'commentsID': u'2693968', 'commentsNum': 145, 'title': 'Google Project Glass modeled by Sergey Brin: first high-res photos ...'}, {'date': '2012-05-17', 'url': 'http://www.theverge.com/2012/5/17/3026571/google-project-glass-infrared-ring-patent', 'commentsID': u'2790612', 'commentsNum': 72, 'title': 'Google Project Glass patent shows control system using infrared ...'}, {'date': '2012-04-06', 'url': 'http://www.theverge.com/2012/4/6/2929486/googles-project-glass-sergey-brin', 'commentsID': u'2693527', 'commentsNum': 88, 'title': "Google's Sergey Brin takes Project Glass into the wild | The Verge"}, {'date': '2012-06-26', 'url': 'http://www.theverge.com/2012/6/26/2986317/google-project-glass-wearable-computers-disappoint-me', 'commentsID': u'2750358', 'commentsNum': 96, 'title': 'Project Glass and the epic history of wearable computers | The Verge'}, {'date': '2012-07-06', 'url': 'http://www.theverge.com/2012/7/5/3139586/apple-patent-google-project-glass', 'commentsID': u'2903627', 'commentsNum': 217, 'title': "Intellectual Properly: Apple's patent on Google's Project Glass that ..."}, {'date': '2012-04-04', 'url': 'http://www.theverge.com/2012/4/4/2925237/googles-project-glass-augmented-reality-glasses-begin-testing', 'commentsID': u'2689278', 'commentsNum': 474, 'title': "Google's Project Glass augmented reality glasses begin testing ..."}, {'date': '2012-06-28', 'url': 'http://www.theverge.com/2012/6/28/3123881/sergey-brin-shows-off-his-google-glass-shade-accessory', 'commentsID': u'2887922', 'commentsNum': 42, 'title': 'Sergey Brin shows off his Google Glass shade accessory | The Verge'}, {'date': '2013-01-21', 'url': 'http://www.theverge.com/2013/1/21/3899068/sergey-brin-on-the-subway-wearing-google-project-glass', 'commentsID': u'3663109', 'commentsNum': 244, 'title': 'Sergey Brin rides the NYC subway like a Google boss | The Verge'}, {'date': '2012-05-31', 'url': 'http://www.theverge.com/2012/5/31/3053893/googles-steve-lee-on-project-glass-concept-video-not-just-a', 'commentsID': u'2817934', 'commentsNum': 48, 'title': "Google's Steve Lee on Project Glass: concept video not just a ..."}, {'date': '2012-04-26', 'url': 'http://www.theverge.com/2012/4/26/2977573/google-sebastian-thrun-demonstrates-project-glass-photography', 'commentsID': u'2741614', 'commentsNum': 139, 'title': "Google X founder takes Charlie Rose's picture from Project Glass ..."}, {'date': '2013-02-01', 'url': 'http://www.theverge.com/2013/1/31/3938708/90-seconds-on-the-verge-thursday-january-31st-2013', 'commentsID': u'3702749', 'commentsNum': 0, 'title': 'Video: GTA V, Google Glass, and more - 90 Seconds on The Verge ...'}, {'date': '2012-05-29', 'url': 'http://www.theverge.com/2012/5/29/3051038/sergey-brin-google-project-glass-gavin-newsom', 'commentsID': u'2815079', 'commentsNum': 192, 'title': 'Sergey Brin lets interviewer try on Project Glass, hopes to launch ...'}, {'date': '2012-05-24', 'url': 'http://www.theverge.com/2012/5/23/3040004/sergey-brin-max-braun-project-glass-photography', 'commentsID': u'2804045', 'commentsNum': 32, 'title': 'Watch this: Sergey Brin and Max Braun discuss Project Glass ...'}, {'date': '2012-09-10', 'url': 'http://www.theverge.com/2012/9/9/3306494/google-project-glass-dvf-new-york-fashion-week', 'commentsID': u'3070535', 'commentsNum': 82, 'title': 'Google Project Glass makes it onto the runway to record New York ...'}, {'date': '2012-04-06', 'url': 'http://www.theverge.com/2012/4/6/2929669/sergey-brin-interview-project-glass-prototype-feedback-release-time', 'commentsID': u'2693710', 'commentsNum': 105, 'title': "Sergey Brin: Project Glass feedback 'very useful' so far, 'give us time ..."}, {'date': '2012-05-25', 'url': 'http://www.theverge.com/2012/5/25/3042676/google-glass-first-video-sample', 'commentsID': u'2806717', 'commentsNum': 4, 'title': 'Video: Google Glass first video sample | The Verge'}, {'date': '2012-05-10', 'url': 'http://www.theverge.com/2012/5/10/3011789/google-project-glass-engineer-hands-free-photo', 'commentsID': u'2775830', 'commentsNum': 92, 'title': 'Google engineer Sebastian Thrun posts hands-free photo taken with ...'}, {'date': '2012-05-15', 'url': 'http://www.theverge.com/2012/5/15/3021460/google-project-glass-glasses-design-patent', 'commentsID': u'2785501', 'commentsNum': 60, 'title': 'Google patents Project Glass AR glasses design | The Verge'}, {'date': '2012-06-28', 'url': 'http://www.theverge.com/2012/6/28/3123395/how-google-succeeded-where-color-failed', 'commentsID': u'2887436', 'commentsNum': 116, 'title': 'With a simple skydive, Google succeeded where Color failed | The ...'}, {'date': '2012-04-13', 'url': 'http://www.theverge.com/2012/4/12/2945165/Google-project-glass-glasses-mockup', 'commentsID': u'2709206', 'commentsNum': 51, 'title': "How would Google's Project Glass HUD work for those with ..."}, {'date': '2012-11-05', 'url': 'http://www.theverge.com/2012/11/5/3603162/steve-mann-eyetap-surveillance-sousveillance', 'commentsID': u'3367203', 'commentsNum': 37, 'title': 'EyeTap Digital Eye Glass inventor predicts the future of surveillance ...'}, {'date': '2012-07-17', 'url': 'http://www.theverge.com/2012/7/17/3164786/google-project-glass-anti-theft-patent', 'commentsID': u'2928827', 'commentsNum': 56, 'title': 'Google receives approval for Project Glass anti-theft patent | The ...'}, {'date': '2012-04-11', 'url': 'http://www.theverge.com/2012/4/11/2940489/diy-google-project-glass', 'commentsID': u'2704530', 'commentsNum': 31, 'title': 'DIY project makes Google Glasses a reality | The Verge'}, {'date': '2012-06-19', 'url': 'http://www.theverge.com/2012/6/19/3096861/google-project-glass-side-mounted-trackpad-patented', 'commentsID': u'2860902', 'commentsNum': 16, 'title': 'Google gets patent for Project Glass side-mounted trackpads | The ...'}, {'date': '2012-11-02', 'url': 'http://www.theverge.com/2012/11/2/3589280/google-nexus-4-review', 'commentsID': u'3353321', 'commentsNum': 1889, 'title': 'Google Nexus 4 review - The Verge'}, {'date': '2012-06-27', 'url': 'http://www.theverge.com/2012/6/27/3121359/project-glass-skydives-onto-moscone-center', 'commentsID': u'2885400', 'commentsNum': 3, 'title': 'Video: Project Glass skydives onto Moscone Center | The Verge'}, {'date': '2013-02-10', 'url': 'http://www.theverge.com/2013/2/10/3973364/apple-rumored-to-be-developing-ios-based-smartwatch', 'commentsID': u'3737405', 'commentsNum': 399, 'title': "Apple is 'experimenting' with curved glass smartwatch, says NYT ..."}, {'date': '2012-07-29', 'url': 'http://www.theverge.com/2012/7/29/3198083/watch-this-sight-augmented-reality-lenses', 'commentsID': u'2962124', 'commentsNum': 119, 'title': "Watch this: 'Sight,' an incredible vision of an AR-obsessed future ..."}, {'date': '2012-06-29', 'url': 'http://www.theverge.com/2012/6/29/3125515/google-i-o-2012-day-one-keynote-video', 'commentsID': u'2889556', 'commentsNum': 15, 'title': "Watch this: Google's I/O 2012 day one keynote video now live | The ..."}, {'date': '2013-03-01', 'url': 'http://www.theverge.com/2013/2/28/4041942/corning-says-flexible-glass-displays-are-three-years-away', 'commentsID': u'3805983', 'commentsNum': 21, 'title': "Corning's curved Willow Glass won't appear in flexible displays until ..."}, {'date': '2013-01-06', 'url': 'http://www.theverge.com/2013/1/6/3843760/vuzix-m100-smart-glasses-hands-on-beating-project-glass', 'commentsID': u'3607801', 'commentsNum': 36, 'title': 'Vuzix M100 smart glasses: hands on with the contender trying to ...'}, {'date': '2012-04-04', 'url': 'http://www.theverge.com/2012/4/4/2925253/google-project-glass-press-photos', 'commentsID': u'2689294', 'commentsNum': 0, 'title': 'Gallery: Google Project Glass press photos | The Verge'}, {'date': '2013-01-31', 'url': 'http://www.theverge.com/2013/1/31/3936960/grand-theft-auto-v-xbox-360-playstation-3-release-date-september-17th', 'commentsID': u'3701001', 'commentsNum': 82, 'title': "'Grand Theft Auto V' coming to Xbox 360, PlayStation 3 on ..."}, {'date': '2012-06-05', 'url': 'http://www.theverge.com/2012/6/5/3064855/microsoft-xbox-smartglass-preview', 'commentsID': u'2828896', 'commentsNum': 428, 'title': u'Microsoft Xbox SmartGlass: an in\u2011depth preview | The Verge'}, {'date': '2012-06-28', 'url': 'http://www.theverge.com/2012/6/28/3123491/google-vic-gundotra-bradley-horowitz-interview', 'commentsID': u'2887532', 'commentsNum': 153, 'title': "Google's Vic Gundotra and Bradley Horowitz on the future of ..."}, {'date': '2012-10-29', 'url': 'http://www.theverge.com/2012/10/29/3569540/google-nexus-4-preview-price-release-date', 'commentsID': u'3333581', 'commentsNum': 942, 'title': "The Nexus 4: Google's flagship phone lands November 13th for ..."}, {'date': '2012-07-17', 'url': 'http://www.theverge.com/2012/7/17/3164008/steve-mann-mcdonalds-assault-eyetap-digital-eye-glass', 'commentsID': u'2928049', 'commentsNum': 153, 'title': "Man allegedly assaulted in Paris McDonald's over augmented ..."}, {'date': '2012-12-05', 'url': 'http://www.theverge.com/2012/12/5/3732364/best-way-gmail-google-calendar-iphone-how-to', 'commentsID': u'3496405', 'commentsNum': 197, 'title': 'The best way to use Gmail and Google Calendar on your iPhone ...'}, {'date': '2012-02-21', 'url': 'http://www.theverge.com/2012/2/21/2815187/google-heads-up-display-glasses-to-sell-for-250-to-600-this-year-nyt', 'commentsID': u'2579228', 'commentsNum': 123, 'title': 'Google heads-up display glasses to sell for $250 to $600 this year ...'}, {'date': '2012-06-04', 'url': 'http://www.theverge.com/2012/6/4/3062660/microsoft-xbox-smart-glass-app', 'commentsID': u'2826701', 'commentsNum': 153, 'title': 'Microsoft announces Xbox SmartGlass app for Windows 8 - The Verge'}, {'date': '2012-12-17', 'url': 'http://www.theverge.com/2012/12/17/3775680/Colbert-and-Google-chairman-discuss-politics-satire-tolkien', 'commentsID': u'3539721', 'commentsNum': 65, 'title': 'Watch this: Eric Schmidt interviews Stephen Colbert in the nerdiest ...'}, {'date': '2013-01-03', 'url': 'http://www.theverge.com/2013/1/3/3833028/corning-gorilla-glass-3-announced-for-ces-2013', 'commentsID': u'3597069', 'commentsNum': 96, 'title': 'Corning Gorilla Glass 3 to be three times more scratch resistant than ...'}, {'date': '2012-09-27', 'url': 'http://www.theverge.com/2012/9/27/3417918/hitachi-quartz-glass-data-preservation', 'commentsID': u'3181959', 'commentsNum': 60, 'title': 'Hitachi invents quartz glass storage capable of preserving data for ...'}, {'date': '2013-02-21', 'url': 'http://www.theverge.com/2013/2/21/4014596/google-chromebook-pixel-pictures', 'commentsID': u'3778637', 'commentsNum': 9, 'title': 'Gallery: Google Chromebook Pixel photos | The Verge'}, {'date': '2012-06-16', 'url': 'http://www.theverge.com/2012/6/16/3090944/microsoft-xbox-720-kinect-2-kinect-glasses-doc-leak-rumor', 'commentsID': u'2854985', 'commentsNum': 586, 'title': 'Xbox 720 document leak reveals $299 console with Kinect 2 for ...'}, {'date': '2012-11-15', 'url': 'http://www.theverge.com/2012/11/15/3649668/google-ingress-augmented-reality-game-beta', 'commentsID': u'3413709', 'commentsNum': 65, 'title': "Google's 'Ingress' augmented reality game puts Android users into a ..."}, {'date': '2013-02-27', 'url': 'http://www.theverge.com/2013/2/27/4034928/google-settings-app-appears-in-android', 'commentsID': u'3798969', 'commentsNum': 89, 'title': 'PSA: A mysterious Google Settings app may soon appear on your ...'}, {'date': '2012-06-27', 'url': 'http://www.theverge.com/2012/6/27/3121329/liveblog-images-project-glass-google-i-o-2012', 'commentsID': u'2885370', 'commentsNum': 0, 'title': 'Gallery: Liveblog images of Project Glass at Google I/O 2012 | The ...'}, {'date': '2013-02-26', 'url': 'http://www.theverge.com/2013/2/26/4032082/andy-rubin-says-google-has-no-plans-for-retail-stores', 'commentsID': u'3796123', 'commentsNum': 140, 'title': "Andy Rubin says Google 'has no plans' for retail stores | The Verge"}, {'date': '2012-10-15', 'url': 'http://www.theverge.com/2012/10/15/3507206/microsoft-smart-glass-dance-central-3-hands-on-video', 'commentsID': u'3271247', 'commentsNum': 55, 'title': "Microsoft SmartGlass in action as Dance Central 3's second-screen ..."}, {'date': '2012-12-13', 'url': 'http://www.theverge.com/2012/12/13/3763496/rework-philip-glass-beck-app', 'commentsID': u'3527537', 'commentsNum': 12, 'title': "New 'Rework_' app explores remixed Philip Glass tracks through art ..."}, {'date': '2013-02-21', 'url': 'http://www.theverge.com/2013/2/21/4013480/google-chromebook-pixel', 'commentsID': u'3777521', 'commentsNum': 1018, 'title': 'Google announces Chromebook Pixel: a premium Chrome OS ...'}, {'date': '2013-02-28', 'url': 'http://www.theverge.com/web/2013/2/28/4039732/thom-yorke-says-google-apple-have-made-music-worthless', 'commentsID': u'3803773', 'commentsNum': 186, 'title': "Radiohead's Thom Yorke says Google, Apple have made music ..."}, {'date': '2011-12-07', 'url': 'http://www.theverge.com/2011/12/7/2618225/eric-schmidt-le-web-paris-google-tv-majority-all-tvs', 'commentsID': u'2382266', 'commentsNum': 117, 'title': "Eric Schmidt: Google TV on 'majority' of new TVs by summer 2012 ..."}, {'date': '2013-02-28', 'url': 'http://www.theverge.com/2013/2/28/4040348/google-cfo-products-in-motorola-pipeline-arent-wow-by-google-standards', 'commentsID': u'3804389', 'commentsNum': 238, 'title': "Google's CFO says Motorola's products aren't 'wow' by Google ..."}, {'date': '2012-12-13', 'url': 'http://www.theverge.com/2012/12/12/3760750/google-maps-for-iphone-press-image-gallery', 'commentsID': u'3524791', 'commentsNum': 0, 'title': 'Gallery: Google Maps for iPhone press image gallery | The Verge'}, {'date': '2012-06-26', 'url': 'http://www.theverge.com/2012/6/26/3118716/google-io-2012-day-one-keynote-time-date', 'commentsID': u'2882757', 'commentsNum': 105, 'title': "Our live blog of Google I/O 2012's day one keynote starts today at 9 ..."}, {'date': '2012-10-29', 'url': 'http://www.theverge.com/2012/10/11/3487808/lg-google-nexus-4', 'commentsID': 0, 'title': "From rumor to retail: the full story of Google's fourth-generation ..."}, {'date': '2012-12-13', 'url': 'http://www.theverge.com/2012/12/12/3760770/google-maps-iphone-available-features-navigation-transit', 'commentsID': u'3524811', 'commentsNum': 1059, 'title': 'Google Maps for iPhone is here: how data and design beat Apple ...'}, {'date': '2012-06-06', 'url': 'http://www.theverge.com/2012/6/6/3068231/google-maps', 'commentsID': u'2832272', 'commentsNum': 274, 'title': 'Google Earth to get radically better 3D images, new UI on iOS and ...'}, {'date': '2012-07-12', 'url': 'http://www.theverge.com/2012/6/27/3120804/google-i-o-2012-news-everything-you-need-to-know', 'commentsID': 0, 'title': 'Google I/O 2012: everything you need to know | The Verge'}, {'date': '2013-02-15', 'url': 'http://www.theverge.com/2013/2/15/3993410/google-will-reportedly-open-its-own-retail-stores-starting-this-year', 'commentsID': u'3757451', 'commentsNum': 267, 'title': 'Google will reportedly open its own retail stores starting this year ...'}, {'date': '2012-08-26', 'url': 'http://www.theverge.com/2012/8/26/3269696/spherical-glass-solar-energy-generator', 'commentsID': u'3033737', 'commentsNum': 26, 'title': "Eco-friendly art: Andre Broessel's glass orb helps maximize solar ..."}, {'date': '2011-12-20', 'url': 'http://www.theverge.com/2011/12/19/2647487/google-heads-up-display-eyeglasses-wearable-computer', 'commentsID': u'2411528', 'commentsNum': 50, 'title': 'Google developing heads-up display eyeglasses? | The Verge'}, {'date': '2012-10-18', 'url': 'http://www.theverge.com/2012/10/17/3519032/google-android-event-oct-29-announcement', 'commentsID': u'3283073', 'commentsNum': 744, 'title': 'Google announces Android event for October 29th at 10AM ET | The ...'}, {'date': '2012-07-02', 'url': 'http://www.theverge.com/2012/6/27/3121011/google-i-o-highlights-news-2012-nexus-7-nexus-q', 'commentsID': 0, 'title': 'Google I/O highlights: Nexus 7 tablet, Android 4.1 Jelly Bean, and ...'}, {'date': '2012-11-27', 'url': 'http://www.theverge.com/2012/11/27/3692738/ori-allon-urban-compass-twitter-google-goldman-sachs', 'commentsID': u'3456779', 'commentsNum': 20, 'title': 'After cashing out to Google and Twitter, Ori Allon is going all in with ...'}, {'date': '2012-06-29', 'url': 'http://www.theverge.com/2012/6/29/3125396/google-nexus-7-review', 'commentsID': u'2889437', 'commentsNum': 1185, 'title': 'Google Nexus 7 review | The Verge'}, {'date': '2013-02-23', 'url': 'http://www.theverge.com/2013/2/22/4019552/google-talks-subscription-music-but-launch-not-imminent', 'commentsID': u'3783593', 'commentsNum': 75, 'title': 'Google negotiating for subscription music service to launch in third ...'}, {'date': '2012-11-13', 'url': 'http://www.theverge.com/2012/11/13/3639016/google-books-scanner-vacuum-diy', 'commentsID': u'3403057', 'commentsNum': 34, 'title': 'Google engineer builds $1,500 page-turning scanner out of sheet ...'}, {'date': '2013-02-26', 'url': 'http://www.theverge.com/2013/2/26/4031206/google-selling-phones-in-the-play-store-is-here-to-stay', 'commentsID': u'3795247', 'commentsNum': 104, 'title': "Google: selling phones in the Play store is 'here to stay' | The Verge"}, {'date': '2012-12-30', 'url': 'http://www.theverge.com/2012/12/30/3818530/twitpic-flagged-by-google-as-suspicious', 'commentsID': u'3582571', 'commentsNum': 51, 'title': "TwitPic and some Twitter pages blocked behind Google's anti ..."}]


# Must have '+' 
# print searchFromTheVerge("ios+6")

# print countComments(rBB)
# print countComments(rIOS)
# print countComments(rJellyBean)
# print countComments(rWP8)
# print countComments(rPalmOS)
# print countComments(rAndroidSorted)
# print countComments(rGoogleGlass)
#
# sortUrl(rWindowsPhone)
# print rWindowsPhone
# extractComments(rAndroid, "data_Android_comments.txt")
# extractComments(rBB, "data_BB_comments.txt")
# extractComments(ios, "data_ios_comments.txt")
# extractComments(rWindowsPhone, "data_WindowsPhone_comments.txt")
# ios = sumByMonth(ios_cl)
# bb = sumByMonth(bb_cl)
# jelly = sumByMonth(jellybean_cl)
# wp8 = sumByMonth(wp8_cl)

# j = simplejson.dumps(ios)

#extractComments(rBB, "bb.txt")

# print buildCommentsList(rWP8Sorted)
