#!/usr/bin/python
import sys

def main(argv):
	idx = 0
	nlenerr = 0.0
	sumlen = [0,0,0,0]
	for line in sys.stdin:
		if idx == 0:
			print line
		elif idx % 100 == 0:
			print >> sys.stderr, str(idx) + "th line"
			if nlenerr > 0:
				print >> sys.stderr, str(nlenerr)
				print >> sys.stderr, "%d\t%d\t%d\t%d" % (sumlen[0],sumlen[1],sumlen[2],sumlen[3])
		if len(line.split('\t')) < 4:
			nlenerr += 1
			sumlen[len(line.split('\t'))] += 1
			idx += 1
			continue
		data = line.split('\t')
		words = data[0].split()
		for word in words:
			if word.lower() == 'alcohol':
				print >> sys.stdout, 'alcohol-%s\t%s\t%s' % (data[1],data[2],data[3])
			if word.lower() == 'religion':
				print >> sys.stdout, 'religion-%s\t%s\t%s' % (data[1],data[2],data[3])
			if word.lower() == 'aardvark':
				print >> sys.stdout, 'aardvark-%s\t%s\t%s' % (data[1],data[2],data[3])
		idx += 1


if __name__ == "__main__": 
	main(sys.argv) 
