# -*- coding: utf-8 -*-
"""
    CodingChallenge.p119
    ~~~~~~~~~~~~~~~~~~~~~~~
    Problem 119 Module
"""

import math, time

class Number(object):
    """
    Represents a number
    """
    def __init__(self, val):
        """
        Sets the initial value of the number
        """
        self.val = val
    
    @property
    def sum_digits(self):
        """
        Returns the sum of the digits of a number
        """
        total = 0
        copy_of_val = self.val
        while copy_of_val:
            total, copy_of_val = total + copy_of_val % 10, copy_of_val // 10
        return total  

    def square(self, n):
        """
        Returns the n'th square of a number
        """
        return self.val ** n    


def solution():
    """
    Two loops are used to iterate through the base and exponent. The sum of the
    digits of the exponent is compared to the base. If the two values are equal,
    the base is added to the list. Because the values may appear out of order,
    it is sorted, and the 29th index is returned due to initial 0-indexing of the
    array. 
    """
    start = time.time()
    array = []
    for base in range(5,70):
        base = Number(base)
        for exponent in range (2,20):
            square = Number(base.square(exponent))
            if square.sum_digits == base.val:
                array.append(square.val)
    array.sort()
    end = time.time() - start
    return array[29],end

if __name__ == "__main__":
    result,time = solution()
    print("Result: %s" % result)
    print("---  %2f seconds ---" % (time))