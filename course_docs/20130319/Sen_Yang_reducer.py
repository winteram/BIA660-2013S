#Author: Sen Yang
#reduce function

#Please use the following command to test the program under the directory course_docs/20130319:
# cat example_input_3gram.txt | python Sen_Yang_mapper.py |sort| python Sen_Yang_reducer.py

from operator import itemgetter
import sys

current_word = None
current_year = None
current_occ = 0
current_pages = 0
word = None


# input comes from stand input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input from mapper.py
    word, year, occ, pages = line.split('\t')

    # convert string to float
    try:
        occ = float(occ)
        pages = float(pages)
    except ValueError:
        continue

    if ((current_word == word) and (current_year == year)):
        current_occ += occ
        current_pages += pages
    else:
        if current_word and current_year:
            print '%s\t%s\t%-10.3f' % (current_word, current_year, current_occ/current_pages)
        current_word = word
        current_year = year
        current_occ = occ
        current_pages = pages

# output the last word!
if ((current_word == word) and (current_year == year)):
            print '%s\t%s\t%-10.3f' % (current_word, current_year, current_occ/current_pages)