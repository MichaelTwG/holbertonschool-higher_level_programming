#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    """
        Unitests for max_integer
    """

    def text_empty(self):
        self.assertEqual(max_integer([]), None)

    def text_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def text_max_beggining(self):
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)

    def text_negative_values(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def text_negative_and_positive(self):
        self.assertEqual(max_integer([1, 3, -6, 5]), 5)


if __name__ == '__main__':
    unittest.main()
