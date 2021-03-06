#!/usr/bin/env python

"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

fourMillion = 4000000
f1 = 1
f2 = 2
sum = 0
while f1 <= fourMillion:
    if f2%2 == 0:
        sum += f2
    fnext = f1 + f2
    f1 = f2
    f2 = fnext

print(sum)
