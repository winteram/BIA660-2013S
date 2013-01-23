# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

d = ['a','b','c']

# <codecell>

d

# <codecell>

d[1]

# <codecell>

d[0]

# <codecell>

x = ['x','y','z']

# <codecell>

x

# <codecell>

d

# <codecell>

d + x

# <codecell>

d + ['b']

# <codecell>

d = d + x + ['b']

# <codecell>

d

# <codecell>

d.remove('b')

# <codecell>

d

# <codecell>

d.pop()

# <codecell>

d

# <codecell>

d.insert(1,'b')

# <codecell>

d

# <codecell>

del d[1:3]

# <codecell>

d

# <codecell>

d += x

# <codecell>

d

# <codecell>

for i in range(3):
    d += ['b']

# <codecell>

d

# <codecell>

d.reverse()

# <codecell>

d

# <codecell>

d.sort()

# <codecell>

d

# <codecell>

d += x
d

# <codecell>

f = d.sort()
f
d

# <codecell>

f

# <codecell>

d = ['c','b','a']
d += x
d

# <codecell>

f = d
f.sort()
f
d

# <codecell>

f

# <codecell>

d

# <codecell>

d

# <codecell>

d

# <codecell>

f

# <codecell>

range(3)

# <codecell>

[x*2 for x in range(6)]

# <codecell>

x = []
for i in range(6):
    x.append(i*2)
x

# <codecell>

x

# <codecell>

x = range(10)
x

# <codecell>

[i for i in range(10) if i % 2 == 1]

# <codecell>

di = {'a':1,'b':2,'c':3}
di

# <codecell>

di['a']

# <codecell>

di['c']

# <codecell>

di['d']

# <codecell>

'd' in di

# <codecell>

'c' in di

# <codecell>

di['d'] = 4

# <codecell>

di

# <codecell>

di['a'] = 0

# <codecell>

di

# <codecell>

del di['a']
di

# <codecell>

di.keys()

# <codecell>

di.values()

# <codecell>

di.items()

# <codecell>

for k,v in di.items():
    print k
    print v

# <codecell>

['%s=%s' % (c,d) for c,d in di.items()]

# <codecell>

'%.2f is the number' % 2.56789

# <codecell>

"abc" + "def"

# <codecell>

str1 = "name1,name2,name3,name4"

# <codecell>

str1 += ",name5"

# <codecell>

str1

# <codecell>

strlist = str1.split(',')

# <codecell>

strlist

# <codecell>

strlist[3]

# <codecell>

str1

# <codecell>

strlist2 = str1.split('n')

# <codecell>

strlist2[2]

# <codecell>

strlist2

# <codecell>

'n'.join(strlist2)

# <codecell>

'd'.join(strlist2)

# <codecell>

str1.find('name3')

# <codecell>

str1[12:]

# <codecell>

str1.upper()

# <codecell>

str2 = str1.upper()

# <codecell>

str2

# <codecell>

str2.lower()

# <codecell>

str2

# <codecell>

str2.find('name')

# <codecell>

str2.lower().find('name')

# <codecell>

str2

# <codecell>

str1

# <codecell>

str1.title()

# <codecell>

a = 5
b = 5
c = 6

# <codecell>

if b == a:
    print "Equal"
else:
    print "Not equal"

# <codecell>

a == b and "Equal" or "Not equal"

# <codecell>

False and "Equal" or "Not equal"

# <codecell>

0 and "Equal" or "Not equal"

# <codecell>

'' and "Equal" or "Not equal"

# <codecell>

[] and "Equal" or "Not equal"

# <codecell>

{} and "Equal" or "Not equal"

# <codecell>

() and "Equal" or "Not equal"

# <codecell>

d = ['a','b','c']
if d:
    print "The list is not empty"
else:
    print "The list is empty"

# <codecell>

len(d)

# <codecell>

f = open('test.txt','r')

# <codecell>

f = open('test.txt','w')
f.write("This is a string\n")
f.write("Another line\n")
f.write("Once more with %d numbers\n" % 23)
f.close()

# <codecell>

try:
    f = open('test.txt','r')
except IOError:
    print "File isn't there"
"this line always prints"

# <codecell>

f.mode

# <codecell>

f.name

# <codecell>

for line in f:
    for word in line.split(' '):
        print word

# <codecell>

f.closed

# <codecell>

if not f.closed:
    # open file
    print "file open"
else:
    print "file closed, can open"

# <codecell>

f.close()

# <codecell>

f.closed

# <codecell>

import re

# <codecell>

str1

# <codecell>

m = re.search('name',str1)

# <codecell>

m.group()

# <codecell>

re.findall('name',str1)

# <codecell>

for item in re.finditer('name',str1):
    print item.group()

# <codecell>

m.group()

# <codecell>

m.start()

# <codecell>

m.end()

# <codecell>

str1[m.start():m.end()]

# <codecell>

m.group()

# <codecell>

str3 = "ball bad bury bingo brock"

# <codecell>

re.findall("ba\w+",str3)

# <codecell>

re.findall("ba[A-Za-z0-9_]+",str3)

# <codecell>

re.findall("\w{3,4}",str3)

# <codecell>

re.findall("\w+",str3)

# <codecell>

re.findall("\w?",str3)

# <codecell>

re.findall("\w.",str3)

# <codecell>

str3

# <codecell>

str3 += ' 123 @#$'

# <codecell>

str3

# <codecell>

re.findall('\d+',str3)

# <codecell>

re.findall('\s',str3)

# <codecell>

re.findall('[ilyr]',str3)

# <codecell>

re.findall("[a-d]",str3)

# <codecell>

re.findall("[a-d][a-d]",str3)

# <codecell>

re.findall("[a-d][^a-d ]",str3)

# <codecell>

re.findall("^[a-d][a-d]",str3)

# <codecell>

re.findall("[a-d][^a-d]$",str3)

# <codecell>

str3

# <codecell>

re.split(' [a-d]', str3)

# <codecell>

re.sub(' [a-d]', ',d', str3)

# <codecell>

a = 'abcdef'

# <codecell>

b = 'ghi123'

# <codecell>

for i in a:
    print i
    

# <codecell>

for i in b:
    print ord(i)

# <codecell>

ord('0')

# <codecell>


# <codecell>

b += b

# <codecell>

b

# <codecell>

ord('z')

# <codecell>

122 - 48

# <codecell>

chr(122)

# <codecell>

ord('z')

# <codecell>

chr(122)

# <codecell>

ord('0')

# <codecell>

ord('z')

# <codecell>

26*2 + 10

# <codecell>

allstr = ''
for i in range(32,127):
    allstr += chr(i)
print allstr

# <codecell>

ord('~')

# <codecell>

a = 'direct'

# <codecell>

b = 'pa$$word5'

# <codecell>


