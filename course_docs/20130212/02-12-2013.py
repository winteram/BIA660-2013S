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

print(u'\xAC02')

# <codecell>

unichar = u'\xA0\xAC'

# <codecell>

print unichar.encode('utf-8')

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
phone_string += "(\(?[0-9]{3}\)?)?"  # area code
phone_string += "[-\. ]?" # delimiter
phone_string += "[2-9][0-9]{2}" # prefix
phone_string += "[-\. ]?" # delimiter
phone_string += "[0-9]{4}$" # final four
print phone_string
phone = re.compile(phone_string)

# <codecell>

fh = open('testPhones.txt','r')
phones = fh.readlines()
for ph in phones: 
    if phone.findall(ph):
        print "correct: %s" % ph
    else:
        print "incorrect: %s" % ph

# <codecell>


