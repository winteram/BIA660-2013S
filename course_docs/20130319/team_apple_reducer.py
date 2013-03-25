#!usr/bin/python

import sys
def reducer():
    current_word=None
    current_year=None
    current_occurs=0
    current_pages=0
    for line in sys.stdin:
        word,year,occurs,pages=line.split('\t')

        if word==current_word and year==current_year:
            current_occurs +=int(occurs)
            current_pages +=int(pages)
        else:
            if current_word != None and current_year != None:
                avg=current_occurs/current_pages
                print "word: %s\tyear: %s\tavg: %d" % (current_word,current_year,avg)
            current_word=word
            current_year=year
            current_occurs=int(occurs)
            current_pages=int(pages)

    avg=current_occurs/current_pages
    print "word: %s\tyear: %s\tavg: %d" % (current_word,current_year,avg)

if __name__=="__main__":
    reducer()
