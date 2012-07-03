import unittest
from ikjMultiplication import standardMatrixProduct

class TestCase(unittest.TestCase):
    def setUp(self):
        self.A = [[1,2],[3,4]]
        self.B = [[5,6],[7,8]]
    
    def testSmallQuadraticMultiplication(self):
        C = standardMatrixProduct(self.A, self.B)
        self.assertEquals(C, [[19,22],[43,50]])
