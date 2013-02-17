import re

def emailval():
    fh=open('testEmails.txt','r')
    address=fh.readlines()
    emailaddr=re.compile("[a-z,0-9,A-Z,!#$%&'*+-/=?^_`{|}~.]+@.[a-z,A-Z,0-9]+[\.]*[a-z,A-Z,0-9]+$")
    for ad in address:
        m=emailaddr.match(ad)
        if m:
            print "Correct Email: %s" % ad
        else: 
            print "Incorrect Email: %s" % ad