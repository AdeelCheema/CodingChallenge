# -*- coding: utf-8 -*-
"""
    CodingChallenge.p102
    ~~~~~~~~~~~~~~~~~~~~~~~
    Problem 102 Module
"""

import math, time

class Triangle(object):
    """
    The triangle class is used to represent a triangle
    """
    def __init__(self, ax, ay, bx, by, cx, cy):
        """
        Sets initial coordinates to triangle vertices
        """
        self.A = (float(ax), float(ay))
        self.B = (float(bx), float(by))
        self.C = (float(cx), float(cy))

    @property
    def vertices(self):
        """
        Returns the vertices of a triangle in a tuple
        """
        return (self.A, self.B, self.C)

    def contains_origin(self):
        """
        Returns True if the Triangle contains the origin. This value is calculated by 
        splitting up the triangle into three smaller triangles, each with two vertices 
        of the original and one new vertex as the origin. The summation of the areas
        of these three triangles must equal the area of the original triangle.
        """
        A,B,C = self.vertices
        triangle_area = self.area()
        triangle_ab = Triangle(A[0], A[1], B[0], B[1], 0, 0)
        triangle_ac = Triangle(A[0], A[1], C[0], C[1], 0, 0)
        triangle_bc = Triangle(B[0], B[1], C[0], C[1], 0, 0)
        total_area = triangle_ab.area() + triangle_ac.area() + triangle_bc.area()
        return triangle_area == total_area

    
    def area(self):
        """
        Returns the area of the triangle given its vertices using the shoelace formula
        https://en.wikipedia.org/wiki/Shoelace_formula

        """
        A,B,C = self.vertices
        return math.fabs((A[0] - C[0])*(B[1] - A[1]) - (A[0]-B[0])*(C[1]-A[1]))/2

def solution():
    """
    Input list of triangles from provided file as triangles and count number of triangles
    which pass triangle.contains_origin()
    """
    start = time.time()
    total = 0
    f = open('p102_triangles.txt', 'r')
    for line in f.readlines():
        triangle = Triangle(*line.split(","))
        if triangle.contains_origin():
            total += 1
    f.close()
    end = time.time() - start
    return total, end

if __name__ == "__main__":
    result, time = solution()
    print("Result: %s" % result)
    print("---  %2f seconds ---" % (time))