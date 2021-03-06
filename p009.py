#!/usr/bin/env python

"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagoreanTriplet():
    sum = 1000
    for a in range(1, int(sum/3)):
        b = a+1
        for b in range(1, int(sum/2)):
            c = sum - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

print(pythagoreanTriplet())
