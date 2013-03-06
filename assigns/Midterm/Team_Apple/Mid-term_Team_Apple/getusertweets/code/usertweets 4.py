import tweepy
import string
#authentication
consumer_key='e4c9dytQmwvHySYbGU1GyA'
consumer_secrect='IXhW9JI7LpKv4M1udVj4gP3szJMWJHaEIpx0kKgbD4'
access='1228808310-usnkitugImLJswKvge87CrpxPuENBgxjJ55zdhC'
access_secrect='jTRknnwC5ijtoVkVbnVAYQgJgf3wqhjGOWCh2mKF7IQ'

auth=tweepy.auth.OAuthHandler(consumer_key,consumer_secrect)
auth.set_access_token(access,access_secrect)
count=1

class mylistener(tweepy.StreamListener):
    def on_status(self,status):
        global count
        #As the plaintext file does not support unicode, it will return
        #error when write unicode to it. Therefore we can use this to kind of
        #remove non-English tweets
        try:
            forwrite='%s\n' % status.text
            f.write(forwrite)
            print '%s\n%s\n%d\n' % (status.text,status.created_at,count)
            count +=1
            if count > 50000:
                streamer.disconnect()
        except:
            pass

    def on_error(self,status_code):
        print 'error! error_code=%s' % status_code
        return True  #keep connecting
    def on_limit(self,track):
        print 'limit! track=%s' % track
    def on_timeout(self):
        print 'snoozing Zzzzz..'
        return True  #keep connecting

f1=open('D:\python_midterm\\try\userid.txt','r')
userids=[]
for i in range(0,15000):
    f1.readline()
for i in range(0,5000):
    userid=string.atoi(f1.readline())
    userids.append(userid)
f1.close()
    
f=open('D:\python_midterm\status\usertweets4.txt','w')
lis=mylistener()
streamer=tweepy.Stream(auth=auth,listener=lis,timeout=60)
streamer.filter(follow=userids)
f.write('count=%d' % (count-1))
f.close()
