#!/usr/bin/python

# Core Library modules
from optparse import OptionParser

# Third party modules
import numpy

parser = OptionParser()
parser.add_option(
    "-i",
    dest="filename",
    default="../Testing/5161x7058.in",
    help="input file with matrix J",
    metavar="FILE",
)
(options, args) = parser.parse_args()


def read(filename):
    lines = open(filename).read().splitlines()
    J = []
    for line in lines:
        J.append(map(float, line.split("\t")))
    return numpy.matrix(J)


def print_matrix(matrix):
    matrix = numpy.array(matrix)
    for line in matrix:
        print("\t".join(map(str, line)))


J = read(options.filename)
R = J * J.T
print_matrix(R)
