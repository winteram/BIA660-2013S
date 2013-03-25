#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        try:
            words,year,occurs,pages,books=line.split('\t')
        #output the keywords and values
            for word in words.split():
                if word=='alcohol' or word=='religion':
                    print "%s\t%s\t%s\t%s" % (word,year,occurs,pages)

        except:
            return 0

if __name__=="__main__":
    mapper()
