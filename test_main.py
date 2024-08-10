import unittest

from main import multiply, divide


class TestMain(unittest.TestCase):
    """
    Assert that the multiply function returns the product of two numbers.
    """
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)


    """
    Assert that the division function returns the division of two numbers.
    """
    def test_divide(self):
        self.assertEqual(divide(12, 4), 3)


if __name__ == '__main__':
    unittest.main()
