from operator import itemgetter
import sys








def reducer():
    current_word = None
    current_count = 0
    current_pages= 0
    current_year = 0
    word = None
    #for lines in open("input.txt"):
    for lines in sys.stdin:
        words, year,count,pages,books = lines.split('\t')
        #word, count = line.split('\t')
        count = int(count)
        pages = int(pages)
        year = int(year)
    #for word in words.split():
        #if word == "alcohol":
            #curr
            
            
    
        for word in words.split():
            #print word
            if word == "alcohol":
                if current_word == word and current_year == year:
                    #if current_year = year:
                    current_count += count
                    current_pages += pages
                    #current_year = year
                else:
                    if current_word != None and current_year != None:
                    #if current_word == "alcohol":
                        #print '%s\t%s' % (current_word, current_count)
                        print '%s %s\t%s' % (current_word, current_year, current_count*1.0/current_pages*1.0)
                #if current_word == "religion":
                    #print '%s\t%s' % (current_word, current_count)
                    #print '%s\t%s\t%s' % (current_word, year, current_count*1.0/current_pages*1.0)
                    current_count = count
                    current_pages = pages
                    current_word = word
                    current_year = year
            if word == "religion":
                if current_word == word and current_year == year:
                #if current_year = year:
                    current_count += count
                    current_pages += pages
                #current_year = year
                else:
                    if current_word != None and current_year != None:
                    #if current_word == "alcohol":
                        #print '%s\t%s' % (current_word, current_count)
                        print '%s  %s\t%s' % (current_word, current_year, current_count*1.0/current_pages*1.0)
                #if current_word == "religion":
                    #print '%s\t%s' % (current_word, current_count)
                    #print '%s\t%s\t%s' % (current_word, year, current_count*1.0/current_pages*1.0)
                    current_count = count
                    current_pages = pages
                    current_word = word
                    current_year = year
    #if current_word == word:
    print '%s  %s\t%s' % (current_word, current_year,current_count*1.0/current_pages*1.0)

if __name__=="__main__":
    reducer()
