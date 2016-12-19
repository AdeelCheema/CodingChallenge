# -*- coding: utf-8 -*-
"""
    tests.p119
    ~~~~~~~~~~~~~~~~~~~~~~~
    Tests problem 119 from Project Euler
"""

import unittest
import CodingChallenge

class Problem119(unittest.TestCase):    
    def test_value(self):
        """
        Ensure the value of Number(75) is 75
        """
        number1 = CodingChallenge.Number(75)
        self.assertEqual(number1.val, 75)


    def test_sum_digits(self):
        """
        Ensure the sum of the digits 12345678 is 36
        """
        number1 = CodingChallenge.Number(12345678)
        self.assertEqual(number1.sum_digits,36)

    def test_square(self):
        """
        Ensures the square of Number(55) is 3,025
        """
        number1 = CodingChallenge.Number(55)
        self.assertTrue(number1.square(2))


    def test_euler_solution(self):
        """
        Ensures the answer to Problem 119 on Project Euler is 248155780267521
        """
        self.assertEqual(CodingChallenge.solution_119()[0], 248155780267521)

    def test_solution_runtime(self):
        """
        Ensures the runtime is provided for Problem 119
        """
        self.assertTrue(CodingChallenge.solution_119()[1])