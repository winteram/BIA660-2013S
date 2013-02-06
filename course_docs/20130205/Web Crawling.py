# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from bs4 import BeautifulSoup
import urllib2

# <codecell>

pubs_page = urllib2.urlopen("http://smallsocialsystems.com/cv.html")

# <codecell>

pubs_text = pubs_page.read()

# <codecell>

pubs = BeautifulSoup(pubs_text)

# <codecell>

pubs.title

# <codecell>

pubs.head

# <codecell>

pubs.findAll('div',{'class':'buttonwrapper'})

# <codecell>

pubs.findAll('a',{'class':'smallbutton'})

# <codecell>

for link in pubs.findAll('a',{'class':'smallbutton'}):
    print link.string + ": " + link['href']

# <codecell>

for link in pubs.findAll('a'):
    if link.string=='pdf':
        print link['href']

# <codecell>

for listel in pubs.findAll('li'):
    coauthor = listel.find('a',{'class':'coauthor'})
    if coauthor != None:
        print coauthor['href']

# <codecell>

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
pinfashion = opener.open("http://pinterest.com/all/?category=mens_fashion")

# <codecell>

pinfash = pinfashion.read()

# <codecell>

pins = BeautifulSoup(pinfash)

# <codecell>

for pin in pins.findAll('a',{'class':'PinImage ImgLink'}):
    print pin['href']

# <codecell>

import twitter

# <codecell>

api = twitter.Api(consumer_secret='xr0nXTJytnMdN7XIsoUIGNErJ5QuPJYv92VfBJnX8XI',consumer_key='HrI9pkJWwsdTL1jv9fDmg',access_token_key='19202628-uzTh3h9JB6pM07JaB4fqA4oHnWffsd1blEwApA',access_token_secret='bpP3m3anqew88u3MGAWPqFGElUv5RG4zFkEUDkAD2A')

# <codecell>

print api.VerifyCredentials()

# <codecell>

statuses = api.GetUserTimeline()
for status in statuses:
    print status.text

# <codecell>

friends = api.GetFriends()

# <codecell>

for friend in friends:
    print friend.screen_name

# <codecell>

friendsof = api.GetFriends('PatrickMeier')

# <codecell>

for friend in friendsof:
    print friend.screen_name

# <codecell>

twlists = api.GetLists('winteram')

# <codecell>

print str(twlists)

# <codecell>


# <codecell>

geopage = urllib2.urlopen('http://api.infochimps.com/social/demographics/us_census/topline/search?g.radius=1000&g.latitude=30.3&g.longitude=-97.75&apikey=api_test-W1cipwpcdu9Cbd9pmm8D4Cjc469')

# <codecell>

geocontent = geopage.read()

# <codecell>

import json

# <codecell>

geoobj = json.loads(geocontent)

# <codecell>

for point in geoobj['results']:
    print point['coordinates']

# <codecell>


