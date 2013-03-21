

import twitter
import re
import csv
import time
import sys

api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')


sourcegroup=[]
users=[]
content=[]
tweetdict={}


def gettweets(keywords):
    for i in range(0,len(keywords)):
        #print keywords[i]
        someTweets = api.GetSearch(keywords[i])
        for tweet in someTweets:
            
            try:
                #Get screen name
                user_temp=tweet.user.screen_name
                
                user1=user_temp.encode('utf-8')
                user=unicode(str(user1))
            except IOError:
                print 'Error in getting user'
                user="None"
           
            try:
                usero=api.GetUser(user_temp)
            except IOError:
                print 'Error in getting user - User has been suspended'
                usero="None"
            try:
                #Get tweet content
                text_temp=tweet.text.encode('utf-8')
                text=text_temp.replace(","," ")
                
                
            except IOError:
                print 'Error in getting tweet text'
                text="None"
            
            
            try:
                #Get tweet source
                source=tweet.source.encode('utf-8')
                sourceu=re.compile(ur'&gt;(.*?)&lt')
                sourceur=(str(sourceu.search(source).group(1)))
                
            except IOError:
                print 'Error in getting tweet source'
                sourceur="None"

            if usero != "None":
                try:
                    #Get follower numbers
                    followers_temp=twitter.User.GetFollowersCount(usero)
                    followers=followers_temp
                except IOError:
                    print 'Error in getting followers'
                    followers="None"
            else:
                followers="None"
                
            if usero != "None":
                try:
                    #Get status numbers
                    status_temp=twitter.User.GetStatusesCount(usero)
                    status=status_temp
                except IOError:
                    print 'Error in getting status'
                    status="None"
            else:
                status="None"
                    
            if usero != "None":    
                try:
                    #Get list numbers
                    listed_temp=twitter.User.GetListedCount(usero)
                    listed=listed_temp
                except IOError:
                    print 'Error in getting listed'
                    listed="None"
            else:
                listed="None"

            
            if usero !="None":
                try:
                    #Get friends numbers
                    friends_temp=twitter.User.GetFriendsCount(usero)
                    friends=friends_temp
                except IOError:
                    print 'Error in getting friends'
                    friends="None"
            else:
                friends="None"
            
            
            try:
                #Get tweet date
                date_temp=tweet.created_at
                date=date_temp.encode('utf-8')
                date=date.replace(","," ")
            except IOError:
                print 'Error in getting date'
                date="None"
            
            
            #print date

            #Get retweet count
            if tweet.retweet_count == None:
                retweet="0"
            else:
                retweet_temp=tweet.retweet_count
                retweet=retweet_temp.encode('utf-8')
            #print retweet
                
            
            
            key=str(date)+'-'+str(user)
            
            if key not in tweetdict:
                tweetdict[key]=(user, date,sourceur, retweet,text,followers, status,listed,friends)
                writer.writerow([user, date,sourceur, retweet,text,followers,status,listed,friends])
    print len(tweetdict)
   
    return tweetdict
#print tweetdict


if __name__=="__main__":
    try:
        f = open("tweets.csv","r+")
        print "f open"
    except IOError:
        print "Error opening tweets.csv"
        sys.exit(0)
    else:
        writer=csv.writer(f)
        row = [ "user", "date", "source", "retweets", "tweet",
           "followers","statuses", "listed","friends"]
        writer.writerow(row)
        reader=csv.reader(f)
        tweetdict = {rows[0]:rows[8] for rows in reader}
        print len(tweetdict)

    for j in range(0,800):
        print j
        keywords=['Android','Android OS','Ios','Blackberry','Blackberry OS','IPhone OS', 'Windows Phone OS']
        tweetdict2 = gettweets(keywords)
    

    f.close()

