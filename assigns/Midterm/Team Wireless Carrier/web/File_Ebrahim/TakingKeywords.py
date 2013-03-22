print "loading packages ..."
import twitter
import json
import time
#from collections import Counter
import en
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





fname="database/New Folder/"+"tweets_iPhone.txt"


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
keywords=en.content.keywords(str(tweetBook), top=100, nouns=True, singularize=True, filters=[])
summary = en.content.categorise(str(tweetBook))
print "tweet keywords are\n"
print keywords

print "\nRatio of emotional words in tweets :", summary.emotions


print"\nNumber of Retrieved tweets = ", lines.__len__()
fname2=fname+".Keywords.txt"
f2=open(fname2,'w')
json.dump(str(keywords), f2)
f2.write("\n")
f2.close()

fname3=fname+".words.txt"
f3=open(fname3,'w')
json.dump(str(len(cntS)), f3)
json.dump(str(cntS), f3)
f3.write("\n")
