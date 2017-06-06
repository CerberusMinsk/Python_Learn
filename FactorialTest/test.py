import unittest

from factorial import factorial



class TestFactorial(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorial(1), 1)

    def test_2(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
	unittest.main()
