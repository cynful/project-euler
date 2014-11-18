"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
#!/usr/bin/python

import math

def isPrime(n):
    if n%2 == 0 and n>2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

largePrime = 600851475143
sqrt = int(math.sqrt(largePrime))
lpf = 0
for i in range(1, sqrt):
    if isPrime(i) and largePrime%i == 0:
       lpf = i

print lpf
