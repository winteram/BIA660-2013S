import sys
def mapper(words):
    for line in sys.stdin:
       #input comes from STDIN (standard input)
    #line = line.strip()
       # remove leading and trailing whitespace
    name,year,occurs,pages,books=line.split()
       # input and split into 5 columns
    nametable=[]
    i=0
    words = name.split()
    #split the words in name byeach
    f = open("book_information.txt",'w')
    #open a .txt file to save the print results
    for word in words:
        #print '%s\t%s' % (word, 1)
        if word == 'alcohol':
            print "%s\t%s\t%s\t%s" % (word,year,occurs,pages)
            #search word alcohol and print the line including four items
        if word == 'religion':
            print "%s\t%s\t%s\t%s" % (word,year,occurs,pages)
            #search word alcohol and print the line including four items
            # If "alcohol" and "religion" appear at the same name,
            #the line of this name will be print twice
            ##nametable.append(i,word)
            ##i=i+1 
            # put the line into a list as a set.
    ##print '%s'%nametable
    f.close()
if __name__=="__main__"
