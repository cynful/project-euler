#!/usr/bin/python

"""
Largest product in a grid
Problem 11

In the 20x20 gride below, four numbers along a diagonal line have been
marked in red.

The product of these numbers is 26 * 63 * 78 * 14 = 1788696

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20x20 grid?
"""

gridmatrix = []
with open('p011_20x20grid.txt') as file20x20grid:
    for line in file20x20grid:
        row = map(int, line.split())
        gridmatrix.append(row)

gridsize = 20
largeProd = 0
for r in range(0, gridsize):
    for c in range(0, gridsize):
        if c+3 < 20:
            r1 = gridmatrix[r][c]
            r2 = gridmatrix[r][c+1]
            r3 = gridmatrix[r][c+2]
            r4 = gridmatrix[r][c+3]
            prod = r1*r2*r3*r4
            if largeProd < prod:
                largeProd = prod
        if r+3 < 20:
            d1 = gridmatrix[r][c]
            d2 = gridmatrix[r+1][c]
            d3 = gridmatrix[r+2][c]
            d4 = gridmatrix[r+3][c]
            prod = d1*d2*d3*d4
            if largeProd < prod:
                largeProd = prod
        if r+3 < 20 and c+3 < 20:
            dr1 = gridmatrix[r][c]
            dr2 = gridmatrix[r+1][c+1]
            dr3 = gridmatrix[r+2][c+2]
            dr4 = gridmatrix[r+3][c+3]
            prod = dr1*dr2*dr3*dr4
            if largeProd < prod:
                largeProd = prod
        if r+3 < 20 and c-3 >= 0:
            dl1 = gridmatrix[r][c]
            dl2 = gridmatrix[r+1][c-1]
            dl3 = gridmatrix[r+2][c-2]
            dl4 = gridmatrix[r+3][c-3]
            prod = dl1*dl2*dl3*dl4
            if largeProd < prod:
                largeProd = prod

print largeProd
