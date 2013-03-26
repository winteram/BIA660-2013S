'''
Home work: Mapper/Reducer
Author: Mengyi Gong
Co-worker: Xiyu Zhu
Date finished at: 3/26/2013

'''
#!usr/bin/python

import sys
def reducer():
    current_year=None
    current_occurs=0.0
    current_pages=0.0
    for line in sys.stdin:
        year,occurs,pages,words=line.split('\t')
        
        if year==current_year:
            current_occurs +=float(occurs)
            current_pages +=float(pages)
        else:
            if current_year:
                avg=float(current_occurs)/float(current_pages)
                print "year: %s average occurrence per page of target 3grams: %s " % (current_year,avg) + "(" + str(float(current_occurs)) + " over " + str(float(current_pages)) + ")"
            current_year=year
            current_occurs=int(occurs)
            current_pages=int(pages)

    avg=float(current_occurs)/float(current_pages)
    print "year: %s average occurrence per page of target 3grams: %s " % (current_year,avg) + "(" + str(float(current_occurs)) + " over " + str(float(current_pages)) + ")"

if __name__=="__main__":
    reducer()
