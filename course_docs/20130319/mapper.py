



import sys

for line in sys.stdin:
	if len(line.split('\t')) != 5:
		continue
	ngram,year,N,pg,bk = line.split('\t')
	words = ngram.split()
	for word in words:
		if word.lower() == 'alcohol':
			print('alcohol-%s\t%s\t%s') % (year,N,pg)
		if word.lower() == 'religion':
			print('religion-%s\t%s\t%s') % (year,N,pg)
