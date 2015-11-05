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


def print_matrix(matrix, f):
    for line in matrix:
        f.write("\t".join(map(str, line)) + "\n")


def ikj_matrix_product(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not isfile(x):
        raise argparse.ArgumentError("{0} does not exist".format(x))
    return x


if __name__ == "__main__":
    import argparse
    import sys
    from os.path import isfile
    from argparse import ArgumentParser

    parser = ArgumentParser(description="ikjMatrix multiplication")
    parser.add_argument("-i", "--input",
                        dest="filename",
                        required=True,
                        type=extant_file,
                        help="input file with two matrices",
                        metavar="FILE")
    parser.add_argument("-o", "--output",
                        type=argparse.FileType(mode='w'),
                        default=sys.stdout, dest="output",
                        help="file to write output to (default=stdout)")
    args = parser.parse_args()

    A, B = read(args.filename)
    C = ikj_matrix_product(A, B)
    print_matrix(C, args.output)
