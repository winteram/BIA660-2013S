import twitter
import pprint
import urllib2
import re
import json
import time
# create a pretty printer
pp = pprint.PrettyPrinter(indent=3)

# Number of random tweets to pull
NUMTWEETS = 200

# create interface for Twitter API
api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')

# Get a random selection of tweets from public timeline
someTweets = api.GetSearch('#bigdata')

#pp.pprint(someTweets[0])

first = True
tweets = []
urls = []
location_str = []
friends = []
followers = []
regexurls = re.compile("(https?://)*([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+\.[a-zA-Z]{2,4}(/[a-zA-Z0-9_\(\)\-]*)*")

for tweet in someTweets:
    if first:
    	pp.pprint(tweet)
    	first = False
    if 'text' in tweet:
        tweets.extend(tweet.text)
        urls.extend(regexurls.findall(tweet.text))
        location_str.append(tweet.user.location)
        friends.append(tweet.user.friends_count)
        followers.append(tweetuser.followers_count)

for locstr in location_str:
    #ascii_locstr = "".join((c if ord(c) < 128 else '' for c in locstr))
    ascii_locstr = re.sub("[^a-zA-Z0-9_ \,\.\-]","",locstr)
    print urllib2.quote_plus(ascii_locstr)
    time.sleep(1)
    response = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=" + urllib2.quote_plus(ascii_locstr) + "&sensor=false")
    location_json = response.read()
    try:
        location = json.loads(location_json)
    except:
        print "Error: " + location_json
    else:
        if len(location['results']) > 0:
            print "\t" + location['results'][0]['formatted_address']
            print "\t" + str(location['results'][0]['geometry']['location']['lat']) + "," + str(location['results'][0]['geometry']['location']['lng'])

