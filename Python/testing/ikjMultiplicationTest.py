#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest
sys.path.append("/home/moose/Downloads/matrix-multiplication/Python/")
from ikjMultiplication import ikjMatrixProduct

class TestCase(unittest.TestCase):    
    def test2Multiplication(self):
        A = [[1,2],[3,4]]
        B = [[5,6],[7,8]]
        C = ikjMatrixProduct(A, B)
        self.assertEqual(C, [[19,22],[43,50]])
        
    def test3Multiplication(self):
        A = [[1, 2, 5],[3,4,6],[1,1,1]]
        B = [[5, 6, 7],[7,8,8],[0,9,3]]
        C = ikjMatrixProduct(A, B)
        self.assertEqual(C, [[19,67,38],[43,104,71], [12,23,18]])
        
if __name__ == '__main__':
    unittest.main()
