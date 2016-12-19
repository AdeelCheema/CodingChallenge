# -*- coding: utf-8 -*-
"""
    CodingChallenge.p107
    ~~~~~~~~~~~~~~~~~~~~~~~
    Problem 107 Module
"""

import time

class Node(object):
    """
    The node class represents a node object, which contains a value and
    a rank

    """
    def __init__(self,label):
        self.parent = self
        self.label = label
        self.rank = 0

    def __eq__(self,other):
        return self.label == other.label

class DisjointSet(object):
    """
    The disjoint set class is used to represent a disjoint set, with the ability
    to find and merge, optimized by taking advantage of path compression and 
    ranks

    Reference: http://www.ics.uci.edu/~eppstein/PADS/UnionFind.py

    """
    def __init__(self):
        self.collection = []

    @property
    def sets(self): 
        return self.collection

    def add(self, node):
        self.collection.append(node)

    def find(self, node):
        while node != node.parent:
            node = node.parent
        return node
 
    def union(self, node1, node2):
        root_node_1 = self.find(node1)
        root_node_2 = self.find(node2)
        if root_node_1.rank < root_node_2.rank:
            root_node_1.parent = root_node_2
        elif root_node_1.rank > root_node_2.rank:
            root_node_2.parent = root_node_1
        elif root_node_1 != root_node_2:
            root_node_2.parent = root_node_1
            root_node_1.rank += 1

class MinimalSpanningTree(object):
    """
    The minimal spanning tree class helps determine the minimal spanning tree given
    a set of edges and vertices, using Kruskal's algorithm

    Reference: https://en.wikipedia.org/wiki/Kruskal's_algorithm
    """
    def __init__(self, nodes, edges):
        self.forest = DisjointSet()
        self.current_mst = []
        self.nodes = nodes
        self.edges = edges
        self.size = len(nodes) - 1
        for node in nodes:
            self.forest.add(node)

    def __len__(self):
        return self.size

    @property
    def weight(self):
        total = 0
        for value in self.edges:
            total += value[2]
        return total
    
    @property
    def spanning(self):
        return self.size == 0

    def calculate_spanning_tree(self):
        total_mst_weight = 0
        self.edges.sort(key=lambda x: x[2])

        for edge in self.edges:
            node1, node2, weight = edge
            root_1 = self.forest.find(node1)
            root_2 = self.forest.find(node2)
            if (root_1 is not root_2):
                self.size -= 1
                self.current_mst.append(edge)
                total_mst_weight += edge[2]
                if self.spanning:
                    return self.current_mst, total_mst_weight
                self.forest.union(root_1, root_2)

class SolutionHelper(object):
    """
    The solution helper class contains functions meant to aid in importing the provided
    input file, networks.txt from Project Euler
    """
    def __init__(self, file_name):
        self.lines = []
        f = open (file_name, "r")
        for line in f.read().split('\n'):
                self.lines.append(line.split (","))
        f.close()
        self.size = len(self.lines) - 1
        self.edges = []
        self.nodes = []

    def generate_tree(self):
        total_original_weight = 0

        for vertex in range(0, self.size):
            self.nodes.append(Node(vertex))

        for column in range(0,self.size):
            for row in range(0, column):
                val = self.lines[column][row]
                if val != '-':
                    total_original_weight += int(val)
                    self.edges.append((self.nodes[column], self.nodes[row], int(val)))
        return self.nodes,self.edges,total_original_weight


def solution_107():
    """
    Input list of vertices and edges of a tree, represented as an adjacency list, and
    output the savings of the original tree vs. its minimum spanning tree
    """
    start = time.time()
    helper = SolutionHelper("p107_network.txt")
    nodes,edges,total_weight = helper.generate_tree()
    mst, mst_weight = MinimalSpanningTree(nodes,edges).calculate_spanning_tree()
    end = time.time() - start
    return total_weight - mst_weight, end

if __name__ == "__main__":
    result, time = solution_107()
    print("Result: %s" % result)
    print("---  %2f seconds ---" % (time))