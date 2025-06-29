import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(100, 200), 300)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0) # Test with floats
        self.assertEqual(self.calc.add(-2.5, 2.5), 0.0) # Test with floats

    def test_subtraction(self):
        """Test the subtract method with various numbers."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0) # Test with floats
        self.assertEqual(self.calc.subtract(-10.0, -5.0), -5.0) # Test with floats

    def test_multiplication(self):
        """Test the multiply method with various numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0) # Test with floats
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25) # Test with floats

    def test_division(self):
        """Test the divide method with various numbers, including division by zero."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5) # Test with float result
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(7, -2), -3.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(5, 0)) # Test division by zero
        self.assertIsNone(self.calc.divide(0, 0)) # Test division by zero (edge case)
        self.assertEqual(self.calc.divide(10.0, 4.0), 2.5) # Test with floats

if __name__ == '__main__':
    unittest.main()