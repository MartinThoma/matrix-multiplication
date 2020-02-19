#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing, numpy, ctypes


def read(filename):
    lines = open(filename, "r").read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append([int(el) for el in line.split("\t")])
        else:
            matrix = B
    return A, B


def printMatrix(matrix, f):
    for line in matrix:
        f.write("\t".join([str(el) for el in line]) + "\n")


def lineMult(start):
    global A, B, mp_arr, part
    n = len(A)
    # create a new numpy array using the same memory as mp_arr
    arr = numpy.frombuffer(mp_arr.get_obj(), dtype=ctypes.c_int)
    C = arr.reshape((n, n))
    for i in range(start, start + part):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]


def ikjMatrixProduct(A, B, threadNumber):
    n = len(A)
    pool = multiprocessing.Pool(threadNumber)

    pool.map(lineMult, range(0, n, part))
    # mp_arr and arr share the same memory
    arr = numpy.frombuffer(mp_arr.get_obj(), dtype=ctypes.c_int)
    C = arr.reshape((n, n))
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
    parser.add_argument(
        "-i",
        "--input",
        dest="filename",
        required=True,
        type=extant_file,
        help="input file with two matrices",
        metavar="FILE",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=argparse.FileType(mode="w"),
        default=sys.stdout,
        dest="output",
        help="file to write output to (default=stdout)",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=2,
        dest="threads",
        help="number of threads to use; use power of 2 (default: 2)",
    )
    args = parser.parse_args()

    A, B = read(args.filename)
    n, m, p = len(A), len(A[0]), len(B[0])

    threadNumber = args.threads
    part = len(A) // threadNumber
    if part < 1:
        part = 1

    # shared, can be used from multiple processes
    mp_arr = multiprocessing.Array(ctypes.c_int, n * p)
    C = ikjMatrixProduct(A, B, threadNumber)
    printMatrix(C, args.output)
