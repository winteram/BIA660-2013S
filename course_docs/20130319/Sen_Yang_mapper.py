#Author: Sen Yang
#map functon

import sys

kw1 = 'alcohol'
kw2 = 'religion'
# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    words = line.split('\t')

    if(kw1 in words[0]):
    	print '%s\t%s\t%s\t%s' % (kw1, words[1],words[2],words[3])

    if(kw2 in words[0]):
    	print '%s\t%s\t%s\t%s' % (kw2, words[1],words[2],words[3])