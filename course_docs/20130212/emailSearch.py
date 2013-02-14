import re


match_string = "(^|\s)(?P<user>[a-zA-Z0-9_\-\.\+]+)" # user name
match_string += "@(?P<domain>[a-zA-Z0-9_\-]+)" # domain
match_string += "\.(?P<tld>[a-zA-Z]{2,4})(\s|\. |\.$|$)" # final bit (.com, .edu, .ly, .info)

print match_string

emails = re.compile(match_string)

fh = open("testEmails.txt")

print "Match"
for line in fh:
    isemail = emails.search(line)
    if isemail:
        print "User: " + isemail.group('user')
        print "Domain: " + isemail.group('domain')
        print "Top-level domain: " + isemail.group('tld')

fh.close()
fh = open("testEmails.txt")

print "\n\n"
print "No match"
for line in fh:
    isemail = emails.search(line)
    if isemail == None:
        print line,
