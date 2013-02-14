# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

thisisanumber = 5

# <codecell>

isinstance(thisisanumber, (int,float))

# <codecell>

thisisacharacter ='a'

# <codecell>

isinstance(thisisacharacter, (int,str))

# <codecell>

lat, lon = -143.234543, 90.2345234

# <codecell>

if lat < -90 or lat > 90 or lon < -180 or lon > 180:
    print "invalid location: %f, %f" % (lat,lon)

# <codecell>

assert(lat > -90 and lat < 90)

# <codecell>

print(u'\u2652\u267A\u2661')

# <codecell>

unichar = u'\u2652\u267A\u2661'

# <codecell>

print unichar + "test"

# <codecell>

import time

# <codecell>

time.time()

# <codecell>

time.strftime("%A, %b %d %Y, %I:%M %p",time.localtime())

# <codecell>

time.localtime()

# <codecell>

i_think_this_is_time = "Feb 12, 1988"
i_think_this_is_time = "February 12, 2012 18:59"

try:
    thisdate = time.strptime(i_think_this_is_time,"%b %d, %Y")
except ValueError:
    print i_think_this_is_time + " is not a valid date"
else:
    print thisdate

# <codecell>

import re

# <codecell>

phone_string = "^\+?[0-9]?" # country code
phone_string += "[-\. ]?" # delimiter
phone_string += "(\(?" # optional enclosure
phone_string += "(?P<area>[0-9]{3})"
phone_string += "\)?)?"  # area code
phone_string += "[-\. ]?" # delimiter
phone_string += "(?P<prefix>[2-9][0-9]{2})" # prefix
phone_string += "[-\. ]?" # delimiter
phone_string += "(?P<final>[0-9]{4})$" # final four
print phone_string
phone = re.compile(phone_string)

# <codecell>

fh = open('testPhones.txt','r')
phones = fh.readlines()
for ph in phones: 
    m = phone.match(ph)
    if m:
        d = m.groupdict()
        #print "area: %s, prefix: %s, final: %s" % (d['area'],d['prefix'],d['final'])
        if d['area']:
            print "%s-%s-%s" % (d['area'],d['prefix'],d['final'])
        else:
            print "%s-%s" % (d['prefix'],d['final'])
    else:
        print "incorrect: %s" % ph

# <codecell>

# path_to_file = "C:\Users\path\to\file"
#fh = open(path_to_file+'testPhones.txt','r')
fh = open('testPhones.txt','r')
phones = fh.readlines()
for ph in phones: 
    if phone.findall(ph):
        print "correct: %s" % ph
    else:
        print "incorrect: %s" % ph

# <codecell>

import numpy

# <codecell>

print(u'\u1201\u1261')

# <codecell>

import twitter

api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')

# <codecell>

someTweets = api.GetSearch('starbucks')

# <codecell>

for tweet in someTweets:
    print "User: %s\nTweet: %s\nClient: %s\n\n" % (tweet.user.screen_name,tweet.text,tweet.geo)

# <codecell>


