#!/usr/bin/env python

from pylab import imshow,show
from numpy import loadtxt

data = loadtxt("circular.dat",float)
imshow(data)
show()
