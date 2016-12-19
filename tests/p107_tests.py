# -*- coding: utf-8 -*-
"""
    tests.p107
    ~~~~~~~~~~~~~~~~~~~~~~~
    Tests problem 107 from Project Euler
"""

import unittest
import CodingChallenge

class Problem107_Node_Test(unittest.TestCase):    
    def test_sanity_initialization(self):
        """
        Ensures the parent, label, and rank of Node (1)
        are itself,2,0 respectively
        """
        node1 = CodingChallenge.Node(1)
        self.assertEqual(node1.parent, node1)
        self.assertEqual(node1.label, 1)
        self.assertEqual(node1.rank, 0)

    def test_sanity_equals(self):
        """
        Ensures Node(5) and Node(5) are equal
        """
        node1 = CodingChallenge.Node(5)
        node2 = CodingChallenge.Node(5)
        self.assertEqual(node1, node2)

class Problem107_DisjointSet_Test(unittest.TestCase):    
    def test_sanity_initialization(self):
        """
        Ensures the disjoint set collection is initialized
        as an empty list
        """
        dsj1 = CodingChallenge.DisjointSet()
        self.assertEqual(dsj1.collection, [])

    def test_sanity_sets(self):
        """
        Ensures the sets property return the sets within
        the collection, 10 Node objects should return a length
        of 10
        """
        dsj1 = CodingChallenge.DisjointSet()
        for i in range(0,10):
            dsj1.add(CodingChallenge.Node(i))
        self.assertEqual(len(dsj1.sets), 10)

    def test_union(self):
        """
        Ensures that when individual pairs of Nodes are connected,
        each node2's parent is set correctly to node1's parent, following
        the ranking scheme
        """
        dsj1 = CodingChallenge.DisjointSet()
        for i in range(1, 6):
            dsj1.add(CodingChallenge.Node(i))
        unions = [[1, 2], [2, 4], [4, 5]]
        for u in unions:
            union1 = CodingChallenge.Node(u[0])
            union2 = CodingChallenge.Node(u[1])
            dsj1.union(union1, union2)
            self.assertEqual(union2.parent, union1)

        self.assertEqual(len(dsj1.sets), 5)

    def test_find(self):
        """
        Ensures that the root parent is correct, given a final set
        as follows [[0, 1, 2, 4], [3]]
        """
        dsj1 = CodingChallenge.DisjointSet()
        nodes = []
        for i in range(0, 5):
            node1 = CodingChallenge.Node(i)
            dsj1.add(node1)
            nodes.append(node1)
        unions = [[0, 1], [1, 2], [2,3]]
        for u in unions:
            union1 = nodes[u[0]]
            union2 = nodes[u[1]]
            dsj1.union(union1, union2)
        for node in [0,1,2,3]:
            self.assertEqual(dsj1.find(nodes[node]), nodes[0])
        self.assertEqual(dsj1.find(nodes[4]), nodes[4])

class Problem107_SolutionHelper_Test(unittest.TestCase):
    def test_sanity_helper(self):
        """
        Ensures the SolutionHelper class initializes with correct values, given 
        a variation of the nodes from network.txt
        """
        helper = CodingChallenge.SolutionHelper("p107_test_network.txt")
        nodes,edges,total_weight = helper.generate_tree()
        self.assertEqual(lien(nodes), 40)
        self.assertEqual(len(edges), 513)
        self.assertEqual(total_weight, 261888)

class Problem107_MST_Test(unittest.TestCase):
    def test_sanity_mst(self):
        """
        Ensures the MST class returns the correct MST, given the
        test network: p107_test_network.txt
        """
        helper = CodingChallenge.SolutionHelper("p107_test_network.txt")
        nodes,edges,total_weight = helper.generate_tree()
        mst, mst_weight = CodingChallenge.MinimumSpanningTree(nodes,edges).calculate_spanning_tree()
        self.assertEqual(len(mst), 39)
        self.assertEqual(mst_weight, 2153)

class Problem107_Euler_Test(unittest.TestCase):
    def test_euler_solution(self):
        """
        Ensures the answer to Problem 107 on Project Euler is 259679
        """
        self.assertEqual(CodingChallenge.solution_107()[0], 259679)

    def test_solution_runtime(self):
        """
        Ensures the runtime is provided for Problem 107
        """
        self.assertTrue(CodingChallenge.solution_107()[1])
      
if __name__ == '__main__':
    unittest.main()  
