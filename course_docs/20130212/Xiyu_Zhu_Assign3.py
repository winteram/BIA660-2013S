import re

Email="^[a-zA-Z0-9_-]{1,99}"
Email+="\@"
Email+="[a-zA-Z0-9]{1,99}"
Email+="\."
Email+="[a-zA-Z0-9_-]{1,99}$"

email = re.compile(Email)
fh=open("testEmails.txt")
emails = fh.readlines()

for em in emails:
    if email.findall(em):
        print "correct %s" % em
    else:
        print "incorrect %s" % em

