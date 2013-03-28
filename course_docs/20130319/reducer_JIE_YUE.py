from operator import itemgetter
import sys

current_key = None
current_count_N = 0
current_count_p = 0
key = None

def deducer():
    for line in sys.stdin:
        key, N, p = line.split('\t')
        count_N = int (N)
        count_p = int (p)

        if current_key == key:
            current_count_N += count_N
            current_count_p += count_p
        else:
            if current_key:
            print '%s\t%s\t%s'% (current_key[:-4],current_key[-4:], current_count_N/current_count_p)
            current_count_N = N
            current_count_p = p
            current_key = key

    if current_key == key:
        print '%s\t%s\t%s'% (current_key[:-4],current_key[-4:], current_count_N/current_count_p)
            


 ## team members: Jie Ren and Yue Han           
        
        
