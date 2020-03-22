#!/usr/bin/python
# -*- coding: utf-8 -*-
# cython: language_level=3

# Core Library modules
from optparse import OptionParser

# Third party modules
import library_numpy

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

    library_numpy.main(options.filename)
