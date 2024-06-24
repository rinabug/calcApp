import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
    
    def test_div(self):
	self.assertEqual(self.calc.div(6, 3), 2)
	self.assertEqual(self.calc.div(5, 2), 2.5)

    def test_power(self):
	self.assertEqual(self.calc.power(2, 3), 8)
	self.assertEqual(self.calc.power(5, 0), 1)

    def test_edge_cases(self):
	self.assertEqual(self.calc.add(0, 0), 0)
	self.assertEqual(self.calc.sub(2, 2), 0)
