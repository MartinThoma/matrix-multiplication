#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Create random integer n×n matrices."""

import random
random.seed(1234)


def main(n):
    matrix_a = create_random_matrix(n)
    matrix_b = create_random_matrix(n)
    save_matrix(matrix_a, matrix_b, "%i.in" % n)


def create_random_matrix(n):
    max_val = 1000  # I don't want to get Java / C++ into trouble ;-)
    matrix = []
    for i in range(n):
        matrix.append([random.randint(0, max_val) for el in range(n)])
    return matrix


def save_matrix(matrix_a, matrix_b, filename):
    f = open(filename, 'w')
    for i, matrix in enumerate([matrix_a, matrix_b]):
        if i != 0:
            f.write("\n")
        for line in matrix:
            f.write("\t".join(map(str, line)) + "\n")


def get_parser():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n",
                        dest="n",
                        default=2000,
                        type=int,
                        help="How big should the two matrices be?")
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    main(args.n)
