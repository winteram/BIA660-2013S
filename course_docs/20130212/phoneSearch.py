import re


match_string = "\+*1*[ \-\.]*" # possible leading country code and trailing delimiter

match_string += "(\(*[0-9]{3}\)*)*" # area code

match_string += "[ \.\-]?" # delimiter between area code and phone number

match_string += "[0-9]{3}" # first three digits

match_string += "[\-\. ]?" # possible delimiter

match_string += "[0-9]{4}([ ]|$|\.+ )" # last 4 digits

print match_string

phones = re.compile(match_string)

fh = open("testEmails.txt")

print "Match"
for line in fh:
    isphone = phones.search(line)
    if isphone:
        print isphone.group(0)

fh.close()
fh = open("testPhones.txt")

print "No match"
for line in fh:
    isphone = phones.search(line)
    if isphone == None:
        print line
