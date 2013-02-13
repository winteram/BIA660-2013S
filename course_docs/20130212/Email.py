#Ebrahim Safavi
# and 
#Mahdi Azarafrooz

import re

s= '[a-zA-Z0-9_\.]*'
s+="\@" # @ sign
s+='[a-zA-Z0-9_]*'
s+="\." # . at the end
s+='[a-zA-Z0-9_\.]*'

f=re.compile(s)

em=open('test.txt','r')
for l in em.readlines():
	print f.findall(l)
	


