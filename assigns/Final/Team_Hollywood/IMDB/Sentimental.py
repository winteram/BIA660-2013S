import urllib2

from BeautifulSoup import BeautifulSoup

from mechanize import Browser

import re

def my_comment(n,filmid):
    
# n is number of pages to crawl

    k=10*n #e.g. for n=2, it crawls the latest 20 comments 
    
    i=0
    
    while(i<k):
    
        url='http://www.imdb.com/title/'+filmid+'/reviews?start='+str(i)
        
        page=urllib2.urlopen(url)
        
        soup=BeautifulSoup(page.read())

        rev=soup.findAll('p')
        
        for j in rev:
            
            #print j
            
            j=str(j)
            review.append(j)
        i=i+1
        
def sen():    
    negfh = open("negative.txt",'r')
    posfh = open("positive.txt",'r')
    count_neg = 0
    count_pos = 0
    
    negative_words = [word.strip() for word in negfh ]
    positive_words = [word.strip() for word in posfh ]
    for line in review:
        
        
        a = line.split(' ')
        for i in a:
            
            if (i in negative_words):
                count_neg = count_neg +1
            if  (i in positive_words):
                count_pos = count_pos + 1
                print i
   # print "number of positive words:"
    #print count_neg
    #print "number of negative words:"
    #print count_pos
    #print "percentage"
    output=float(count_pos)/(count_neg+count_pos+1)
    print output
    return output
    



    


# the main function
if __name__ == "__main__":

    review=[]
    f = open("ids.txt", 'r')
    g=open("comments.txt","a")
    file1 = f.readlines()
    for line in file1:
    

        my_comment (3,line.split()[1]) 
        d=sen() #sentimental analysis
        g.write('%s,%s \n'%(line.split()[1],d))
    g.close
    
