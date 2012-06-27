#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
random.seed(1234)

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-n", dest="n", type="int", default=2000,
     help="How big should the two matrices be?")
(options, args) = parser.parse_args()

def createRandomMatrix(n):
	maxVal = 1000 # I don't want to get Java / C++ into trouble ;-)
	matrix = []
	for i in xrange(n):
		matrix.append([random.randint(0, maxVal) for el in xrange(n)])
	return matrix

def saveMatrix(matrixA, matrixB, filename):
	f = open(filename, 'w')
	for i, matrix in enumerate([matrixA, matrixB]):
		if i != 0:
			f.write("\n")
		for line in matrix:
			f.write("\t".join(map(str, line)) + "\n")
n = options.n
matrixA = createRandomMatrix(n)
matrixB = createRandomMatrix(n)
saveMatrix(matrixA, matrixB, str(n) + ".in")
