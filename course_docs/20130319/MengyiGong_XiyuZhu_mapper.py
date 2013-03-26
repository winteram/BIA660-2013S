'''
Home work: Mapper/Reducer
Author: Mengyi Gong
Co-worker: Xiyu Zhu
Date finished at: 3/26/2013

'''
#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        try:
            words,year,occurs,pages,books=line.split('\t')
        #output the keywords and values
            for word in words.split():
                if word=='alcohol' or word=='religion':
                    #avg = float(occurs)/float(pages)
                    print "%s\t%s\t%s\t%s" % (year,occurs,pages,words)
        except:
            return 0

if __name__=="__main__":
    mapper()
