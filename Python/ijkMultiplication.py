#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Read two matrices, multiply them, write the result to standard output."""

from optparse import OptionParser

try:
    xrange
except NameError:
    xrange = range


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


def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))


def standard_matrix_product(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i",
                      dest="filename",
                      default="2000.in",
                      help="input file with two matrices",
                      metavar="FILE")
    (options, args) = parser.parse_args()

    A, B = read(options.filename)
    C = standard_matrix_product(A, B)
    print_matrix(C)
