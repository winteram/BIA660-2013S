import tweepy
#authentication
consumer_key='wq66pSnuxYAkPaJDVYTFQ'
consumer_secrect='BsPOvDVZ7i8zIxiO7fxJC9H2w8JsViIpR6jn7htuU'
access='1228808310-RgGp2iiJtPGul6LUQ1IznkQTomTJqcDrvGvZDJ2'
access_secrect='7nOWiUoHZi6mLqQ1yaVBXmSDgTZOKCyL7HRiT7GY'

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

f=open('D:\python_midterm\status\\android.txt','w')
lis=mylistener()
streamer=tweepy.Stream(auth=auth,listener=lis,timeout=60)
streamer.filter(track=['android'])
f.write('count=%d' % (count-1))
f.close()
