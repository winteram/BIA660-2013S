#from operator import itemgetter
import sys

current_key = None
current_N = 0.0
current_pg = 0.0
key = None

for line in sys.stdin:
	key, N, pg = line.split('\t')
	N = float(N)
	pg = float(pg)

	if current_key == key:
		current_N += N
		current_pg += pg
	else:
		if current_key:
			word,year = current_key.split('-')
			print '%s\t%s\t%f' % (word, year, current_N/current_pg)
		current_N = N
		current_pg = pg
		current_key = key

if current_key == key:
	word,year = current_key.split('-')
	print '%s\t%s\t%f' % (word, year, current_N/current_pg)
