#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing, numpy, ctypes

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

def printMatrix(matrix, f):
    for line in matrix:
        f.write("\t".join(map(str,line)) + "\n")

def lineMult(start):
    global A, B, C, part
    n = len(A)
    for i in xrange(start, start+part):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]

def ikjMatrixProduct(A, B, threadNumber):
    n = len(A)
    pool = multiprocessing.Pool(threadNumber)

    pool.map(lineMult, range(0,n, part))
    return C

def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not isfile(x):
        raise argparse.ArgumentError("{0} does not exist".format(x))
    return x

if __name__ == "__main__":
    import argparse, sys
    from os.path import isfile
    from argparse import ArgumentParser

    parser = ArgumentParser(description="ikjMatrix multiplication")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=extant_file,
        help="input file with two matrices", metavar="FILE")
    parser.add_argument("-o", "--output",
        type=argparse.FileType(mode='w'),
        default=sys.stdout, dest="output",
        help="file to write output to (default=stdout)")
    args = parser.parse_args()

    A, B = read(args.filename)
    n, m, p = len(A), len(A[0]), len(B[0])

    threadNumber = 2
    part = len(A) / threadNumber
    if part < 1:
	    part = 1

    C = [[0 for i in xrange(n)] for j in xrange(n)]
    C = ikjMatrixProduct(A, B, threadNumber)
    printMatrix(C, args.output)
