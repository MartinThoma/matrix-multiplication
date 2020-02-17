#!/usr/bin/python
# -*- coding: utf-8 -*-

# Core Library modules
from math import ceil, log
from optparse import OptionParser
from strassen import strassen, read, print_matrix

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option(
        "-i",
        dest="filename",
        default="2000.in",
        help="input file with two matrices",
        metavar="FILE",
    )
    (options, args) = parser.parse_args()

    A, B = read(options.filename)

    C = strassen(A, B)
    print_matrix(C)
