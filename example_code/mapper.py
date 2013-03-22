import sys

for line in sys.stdin:
    words = line.split()

    for word in words:
        print '%s\t%s' % (word, 1)
