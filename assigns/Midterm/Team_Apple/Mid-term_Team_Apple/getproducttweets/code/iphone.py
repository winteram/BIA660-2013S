import tweepy
#authentication
consumer_key='7Mk1Te4rMYmhA0WqC1RQ'
consumer_secrect='pByrKXbp8Yc6CyeSQFfvuiT4kMdKKPC1YnduboI6O9k'
access='786990577-vdZ6nmttDneeyoGYFVo31F6PHhp9fd5gbpsZaSus'
access_secrect='S1zeAQY5r5TBbKUJvxrdpKFwTNGtYcjJ3zec9iwqo'

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

f=open('D:\python_midterm\status\iphone.txt','w')
lis=mylistener()
streamer=tweepy.Stream(auth=auth,listener=lis,timeout=60)
streamer.filter(track=['iphone'])
f.write('count=%d' % (count-1))
f.close()
