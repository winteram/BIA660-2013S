import sys
def reduce():
    #i=0
    #j=0
    #identify the variables
    f=open("book_alcohol.txt",'w')
    #open a .txt to save the results
    with open('book_information.txt') as f:
    #open the .txt file
        for line in f:
        #read the file by line and 
            word,year,occurs,pages=line.split()
            if word=='alcohol':
                f=open("book_alcohol.txt",'w')
                #open a .txt to save the results of alcohol
                #i=i+1
                print "%s\t%s\t%s\t%s" % (word,year,occurs,pages)
                f.close()
            if word=='religion':
                f=open("book_religion.txt",'w')
                #open a .txt to save the results of religion
                #j=j+1
                print "%s\t%s\t%s\t%s" % (word,year,occurs,pages)
                f.close()
    f.close()
    #f=open("book_analysis.txt",'w')
    occrstable={}
    pagestable={}
    with open("book_alcohol.txt") as f:
        word,year,occurs,pages=line.split()
        for year in year:
            if year in occrstable:
                occrstable[year]=occrstable[year]+int(occurs)
            else:
                occrstable[year]=int(occurs)
        for year in year:
            if year in pagestable:
                pagestable[year]=pagestable[year]+int(pages)
            else:
                pagestable[year]=int(pages)            
        for year in occrstable:
            avg=occrstable[year]/pagestable[year]
            print"alcohol,%s,%d"%(year,avg)
    occrstable={}
    pagestable={}
    with open("book_religion.txt") as f:
        word,year,occurs,pages=line.split()
        for year in year:
            if year in occrstable:
                occrstable[year]=occrstable[year]+int(occurs)
            else:
                occrstable[year]=int(occurs)
        for year in year:
            if year in pagestable:
                pagestable[year]=pagestable[year]+int(pages)
            else:
                pagestable[year]=int(pages)            
        for year in occrstable:
            avg=occrstable[year]/pagestable[year]
            print"religion,%s,%d"%(year,avg)               
if __name__=="__main__"

