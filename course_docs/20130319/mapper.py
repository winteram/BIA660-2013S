#!/usr/bin/python
import sys

def main(argv):
	idx = 0
	for line in sys.stdin:
		if idx > 0 and idx % 100000 == 0:
			sys.stderr.write('Processed 100000th line\n')
		if len(line.split('\t')) < 4:
			sys.stderr.write('line length problem\n')
			continue
		data = line.split('\t')
		words = data[0].split()
		for word in words:
			if word.lower() == 'alcohol':
				print('alcohol-%s\t%s\t%s') % (data[1],data[2],data[3])
			if word.lower() == 'religion':
				print('religion-%s\t%s\t%s') % (data[1],data[2],data[3])
			if word.lower() == 'aardvark':
				print('aardvark-%s\t%s\t%s') % (data[1],data[2],data[3])
		idx += 1


if __name__ == "__main__": 
	main(sys.argv) 
