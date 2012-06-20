#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
random.seed(1234)

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
n = 3
matrixA = createRandomMatrix(n)
matrixB = createRandomMatrix(n)
saveMatrix(matrixA, matrixB, "bigMatrix.txt")
