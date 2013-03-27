'''
Created on Mar 24, 2013

@author: zbl
'''
import sys

def mapper():
    count = 0
    
    for lines in sys.stdin:
        #print "%s\t %s\t%s\t%s\t%s" % ("word","year","occurs","pages","books")    
    #for lines in open("input.txt"):
        words,year,occurs,pages,books=lines.split('\t')
    #value = n-gram \t year \t occurrences \t pages \t books
    #words = lines.split('n-gram')
    #a, year,high,ave,low=lines.split('\t')
        for word in words.split():
            if word=="alcohol" :
                count = count + 1
                print "%s\t %s\t%s\t%s\t%s" % (word,year,occurs,pages,books)
            if word=="religion":
                count = count + 1
                print "%s %s\t%s\t%s\t%s" % (word,year,occurs,pages,books)

    print "totally " +str(count)
    #try:
#line = sys.stdin
#line = "sdfsad dfsda dsfsad"
#words = line.split(" ")
#print words
#for word in words:
    #print '%s\t%s' % (word, 1)    
    #for word in words:
        #print '%s\t%s' % (word, 1)
        #print word
    #except KeyboardInterrupt:
        #break
if __name__=="__main__":
    mapper()   
    

