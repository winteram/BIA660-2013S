'''Team Apple
Qi Zhu     
Jian Wang
Yulong Luo
'''
import re

match="^[\w\.\+\s]+@\w+\.[(com)(edu)(ly)(COM)]"
email=re.compile(match)
fp=open('email.txt','r')
emailname=fp.readlines()
for line in emailname:
    if email.findall(line):
        print "correct: %s" % line
    elif line =='\n' or line =='---------------------\n':
        print line
    else:
        print "incorrect: %s" % line
fp.close()
        
