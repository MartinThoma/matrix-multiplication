#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", dest="filename", default="bigMatrix.in",
     help="input file with two matrices", metavar="FILE")
(options, args) = parser.parse_args()

def read(filename):
	lines = open(filename, 'r').read().splitlines()
	A = []
	B = []
	matrix = A
	for line in lines:
		if line != "":
			matrix.append(map(int, line.split("\t")))
		else:
			matrix = B
	return A, B

def printMatrix(matrix):
	matrix = numpy.array(matrix)
	for line in matrix:
		print "\t".join(map(str,line))

A, B = read(options.filename)
A = numpy.matrix(A)
B = numpy.matrix(B)
C = A * B # easy and intuitive, isn't it?
printMatrix(C)
