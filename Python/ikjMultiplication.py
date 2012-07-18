#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    for line in matrix:
        print "\t".join(map(str,line))

def ikjMatrixProduct(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="ikjMatrix multiplication")
    parser.add_argument("-i", dest="filename", default="2000.in",
         help="input file with two matrices", metavar="FILE")
    args = parser.parse_args()

    A, B = read(args.filename)
    C = ikjMatrixProduct(A, B)
    printMatrix(C)
