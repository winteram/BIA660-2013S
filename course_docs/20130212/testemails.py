import re


match_string = "[a-z,A-Z,0-9,!#$%&'*+-/=?^_`{|}~.]" # username
match_string += "+@." # the @ sign
match_string += "[a-z,A-Z,0-9]+[\.]*[a-z,A-Z,0-9]+$" # domain address

email = re.compile(match_string)

fh = open("/Users/elroy/Desktop/testgmail.txt")

print "Match"
for line in fh:
    isemail = email.search(line)
    if isemail:
        print isemail.group(0)

fh.close()
fh = open("/Users/elroy/Desktop/testgmail.txt")

print "No match"
for line in fh:
    isemail = email.search(line)
    if isemail == None:
        print line
