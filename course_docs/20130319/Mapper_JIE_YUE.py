import sys
import re

#keywords=['religion', 'alcohol']
#exactMatch = re.compile(r'\b%s\b' % '\\b|\\b'.join(keywords))

def mapper():
    for line in sys.stdin:
        nrgram, year, N, p, b = line.split('\t')
        for word in nrgram.split():
            if word=='religion' or word=='alcohol':
                key=word+year
                print "%s\t%s\t%s"% (key, N, p)
            else:
                continue


if _name_=="_main_":
    mapper()

    


#for line in sys.stdin:
#    exactMatch.findall(line)
    
#words=('religion bar was' ,'1991' ,'30' , '50')





#if 'religion' in words[0].join(','):
#    print ("%s \t %s")%words[1], words[2]/words[3]
#if 'alcohol' in words[0].split(','):
#    print ("%s \t %s")%words[1], words[2]/words[3]

        
                                
                                     

                                     

