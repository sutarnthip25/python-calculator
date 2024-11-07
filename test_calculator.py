import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # acctual output vs. expected output

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2),-3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1,0),1)

    def test_subtract(self):
        self.assertAlmostEqual(self.calc.subtract(5,2),3)

    def test_subtract_2(self):
        self.assertAlmostEqual(self.calc.subtract(-4,-5),1)

    def test_multiply(self):
        self.assertAlmostEqual(self.calc.multiply(-4,-5),20)

    def test_multiply_2(self):
        self.assertAlmostEqual(self.calc.multiply(50,0),0)
    
    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(50,25),2)

    def test_divide_2(self):
        self.assertAlmostEqual(self.calc.divide(50,1),50)

    def test_modulo(self):
        self.assertAlmostEqual(self.calc.modulo(5,2),1)

    def test_modulo_2(self):
        self.assertAlmostEqual(self.calc.modulo(10,4),2)

    
if __name__ == '__main__':
    unittest.main()
