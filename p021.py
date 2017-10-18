#!/usr/bin/env python

"""
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors or 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

def d(n):
    divisorsum = 0
    sqrt = int(math.sqrt(n))
    if n == sqrt*sqrt:
        divisorsum += sqrt
    for i in range(1, sqrt):
        if n%i == 0:
            if i == 1:
                divisorsum += i
            else:
                divisorsum += i + (n//i)
    return divisorsum

amicableLimit = 10000
amicablesum = 0
for a in range(1, amicableLimit+1):
    b = d(a)
    if b > a and b <= amicableLimit:
        if d(b) == a:
            amicablesum += a + b

print(amicablesum)
