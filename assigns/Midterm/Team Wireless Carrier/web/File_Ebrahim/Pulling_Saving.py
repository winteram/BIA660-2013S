print "loading packages ..."
import twitter
import json
import time
from collections import Counter
import en
import graph

print "loading is done!"

#Merge sorting algorithm for a list of numbers with O(nlogn) complexity
def mergeing(ml, mr,index):
    result = []
    i ,j = 0, 0
    while i < len(ml) and j < len(mr):
        if index==0:
            mlc=ml[i]
            mrc=mr[j]
        else:
            mlc=ml[i][index]
            mrc=mr[j][index]

        if mlc >= mrc:
            result.append(ml[i])
            i += 1
        else:
            result.append(mr[j])
            j += 1
    result += ml[i:]
    result += mr[j:]
    return result




def sorting(m,index):

    if len(m) <= 1:
        return m
    middle = int( len(m) / 2 )
    ml = sorting(m[:middle],index)
    mr = sorting(m[middle:],index)
    return mergeing(ml, mr,index)






#Login in twitter

starttime = time.strftime("%d_%H_%M",time.localtime())

print"Twitter Authentication ..."

api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')
print api.VerifyCredentials().name
print"Authentication is done"


print "Pulling data from twitter"

Term='iphone'
fname="tweets_"+Term+starttime+".txt"

tweets=[]

tweets=api.GetSearch(term=Term, geocode=None, since_id=None, per_page=1, page=1, lang='en', show_user='true', query_users=False)
maxID=tweets[0].id

N=1 # number of iterations
NPage=15 # Number of pages (Maximum=15)

L=0 #Accumulative Number of tweets
f=open(fname,'w')

for j in range(N):
    print "Number of iteration = ", j

    for i in range(1,NPage):
#Searching tweets
            tweets=api.GetSearch(term=Term, geocode=None, since_id=None, per_page=100, page=i, lang='en', show_user='true', query_users=False)
            print"Page Number = ", i, " , Tweets per Page = ", tweets.__len__()
            L+=tweets.__len__()


#saving the data base as json
            print"Saving..."
            for t in tweets:
                    if t.id<=maxID:

                        json.dump(str(t), f)
                        f.write("\n")
                        maxID=t.id # Setting to the last ID of the tweets




            print"Successful Saving!"


    print"Waiting ....."
    time.sleep(1)

f.close()
print"Accumulative Number of tweets = ", L

print "Data collectiong is done!"

#reading the data base as json

print"\nRetrieving data..."
f=open(fname)
lines=f.readlines();
f.close()
cnt={}
i=0
tweetBook=[]
emotion=[]
primary=[]
secondary=[]

for l in lines:
	obj=json.loads(json.loads(l[:-1]))
	#print'[',i,']- ', obj['created_at']
#	print'[',i,']- ', obj['text']

	tweetBook.append(obj['text'].upper())
	cat=en.content.categorise(obj['text'])
	emotion.append(cat.emotions)
	primary.append(cat.primary)
	secondary.append(cat.secondary)
	i+=1
	for word in obj['text'].upper().split(' '):
		if cnt.has_key(word):
			cnt[word]+=1
		else:
			cnt[word]=1


cntS=sorting(cnt.items(),1)

#print [x for [x, y] in cntS]
keywords=en.content.keywords(str(tweetBook), top=20, nouns=True, singularize=True, filters=[])
summary = en.content.categorise(str(tweetBook))
print "tweet keywords are\n"
print keywords

print "\nRatio of emotional words in tweets :", summary.emotions


print"\nNumber of Retrieved tweets = ", lines.__len__()


