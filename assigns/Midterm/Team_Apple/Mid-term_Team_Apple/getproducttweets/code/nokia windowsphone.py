import tweepy
#authentication
consumer_key='BVlMmV1jKosG8y2tlvcBg'
consumer_secrect='ocQZBVkD7P4H9UDATYAqwXIwrNAihdFrKj4ttj3Gc'
access='1228808310-z2C2K5B40xJ3OQFvH6eWjPD1Prl38Ys6jkeKben'
access_secrect='Ku3XC1U2eSKLztAmonX2z73S2ZFFrSF2jMNc1DVnbI'

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
            print '%s\n%d\n' % (status.text,count)
            count +=1
            if count > 1000000:
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

f=open('D:\python_midterm\status\windowsphone.txt','w')
lis=mylistener()
streamer=tweepy.Stream(auth=auth,listener=lis,timeout=60)
streamer.filter(track=['windowsphone'])
f.write('count=%d' % (count-1))
f.close()
