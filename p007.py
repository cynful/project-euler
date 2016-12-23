#!/usr/bin/python

"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

def isPrime(n):
    if n%2 == 0 and n>2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

primePlace = 10001
primes = 0
i = 0
while primes <= primePlace:
    i += 1
    if isPrime(i):
        primes += 1

print i
