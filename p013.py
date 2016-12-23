#!/usr/bin/python

"""
Large sum
Problem 13

Work out the first ten digits of the sum of the following one-hundred
50-digit numbers.
"""

list50digit = []
with open('p013_100x50digits.txt') as file50nums:
    for line in file50nums:
        num = int(line.strip())
        list50digit.append(num)

sum = 0
for n in list50digit:
    sum += n

print str(sum)[0:10]
