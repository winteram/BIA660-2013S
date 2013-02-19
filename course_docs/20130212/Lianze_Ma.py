import re
email_string="^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]{1,10}$"
email=re.compile(email_string)

fh=open("testEmails.txt")
emails=fh.readlines()
for ph in emails:
    if email.findall(ph):
        print "correct: %s" % ph
    else:
        print "incorrect: %s" % ph
    
