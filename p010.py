#!/usr/bin/python

"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

def isPrime(n):
    if n==1 or n%2 == 0 and n>2:
        return False
    return all(n%i for i in range(3, int(math.sqrt(n))+1, 2))

twoMillion = 2000000
sum = 0
for i in range(1, twoMillion+1):
    if isPrime(i):
        sum += i

print sum
