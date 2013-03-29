#!/usr/bin/python
import sys

def main(argv):

	current_key = None
	current_N = 0.0
	current_pg = 0.0
	key = None
	
	for line in sys.stdin:
		if len(line.split('\t')) != 3:
			continue
		key, N, pg = line.split('\t')
		try:
			N = float(N)
		except ValueError:
			continue
		try:
			pg = float(pg)
		except ValueError:
			continue

		if current_key == key:
			current_N += N
			current_pg += pg
		else:
			if current_key:
				tokens = current_key.split('-')
				if len(tokens) == 2:
					print '%s\t%s\t%f' % (tokens[0], tokens[1], current_N/current_pg)
		current_N = N
		current_pg = pg
		current_key = key

	if current_key == key:
		word,year = current_key.split('-')
		print '%s\t%s\t%f' % (word, year, current_N/current_pg)


if __name__ == "__main__": 
	main(sys.argv) 
