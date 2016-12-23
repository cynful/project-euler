#!/usr/bin/python

"""
Lattice paths
Problem 15

Starting in the top left corner of a 2x2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right
corner.

How many such routes are there through a 20x20 grid?
"""

gridsize = 20
paths = 1
for i in range(0, gridsize):
    paths *= (2*gridsize) - i
    paths /= i + 1

print paths
