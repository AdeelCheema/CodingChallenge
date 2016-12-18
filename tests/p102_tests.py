# -*- coding: utf-8 -*-
"""
    tests.p102
    ~~~~~~~~~~~~~~~~~~~~~~~
    Tests problem 102 from Project Euler
"""

import unittest
import numpy
import CodingChallenge

class Problem102(unittest.TestCase):    
    def test_vertices(self):
        """
        Ensure the vertices of Triangle: (0,0) (1,0) (0,1) are (0.0, 0.0), (1.0, 0.0), (0.0, 1.0)
        """
        triangle1 = CodingChallenge.Triangle(0,0,1,0,0,1)
        self.assertEqual(triangle1.vertices,((0.0, 0.0), (1.0, 0.0), (0.0, 1.0)))


    def test_area(self):
        """
        Ensure the area of Triangle: (0,0) (1,0) (0,1) is 0.5
        """
        triangle1 = CodingChallenge.Triangle(0,0,1,0,0,1)
        self.assertEqual(triangle1.area(),0.5)

    def test_contains_origin(self):
        """
        Ensures the Triangle: (0,0) (1,0) (0,1) contains the origin
        """
        triangle1 = CodingChallenge.Triangle(0,0,1,0,0,1)
        self.assertTrue(triangle1.contains_origin())

    def test_contains_origin(self):
        """
        Ensures the Triangle: (1,0) (2,0) (1,1) does not contain the origin
        """
        triangle1 = CodingChallenge.Triangle(1,0,2,0,1,1)
        self.assertFalse(triangle1.contains_origin())

    def test_euler_solution(self):
        """
        Ensures the answer to Problem 102 on Project Euler is 228
        """
        self.assertEqual(CodingChallenge.solution()[0], 228)

    def test_solution_runtime(self):
        """
        Ensures the answer to Problem 102 on Project Euler is 228
        """
        self.assertTrue(CodingChallenge.solution()[1],228)