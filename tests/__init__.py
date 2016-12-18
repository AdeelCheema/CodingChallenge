# -*- coding: utf-8 -*-
"""
    Tests
    ~~~~~~~~~~~~~~~~~~~~~~~
    Initial sanity check tests
"""

import unittest
import CodingChallenge

class Initialization(unittest.TestCase):
    def test_initialization(self):
        """
        Ensure the test suite runs by confirming that 1 + 1 = 2
        """
        self.assertEqual(1 + 1, 2)

    def test_import(self):
        """
        Ensure the test suite can import the Coding Challenge files
        """
        try:
            import CodingChallenge
        except ImportError:
            self.fail("Was not able to import the Coding Challenge")
