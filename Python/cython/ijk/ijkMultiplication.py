#!/usr/bin/python

from ijk_multiplication_c import ijk_matrix_product


def read(filename):  #  -> Tuple[List[List[int]], List[List[int]]]
    lines = open(filename).read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append([int(el) for el in line.split("\t")])
        else:
            matrix = B
    return A, B


def print_matrix(matrix, f):
    for line in matrix:
        f.write("\t".join(map(str, line)) + "\n")


def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not isfile(x):
        raise argparse.ArgumentError(f"{x} does not exist")
    return x


if __name__ == "__main__":
    import argparse
    import sys
    from argparse import ArgumentParser
    from os.path import isfile

    parser = ArgumentParser(description="ijkMatrix multiplication")
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
    args = parser.parse_args()

    A, B = read(args.filename)
    C = ijk_matrix_product(A, B)
    print_matrix(C, args.output)
