#!/usr/bin/env python

"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


"""
0 perfect number
-1 deficient
1 abundant
"""
def perfectNum(n):
    divs = [1]
    for i in range(1, n//2+1):
        if n%i == 0:
            divs.append(i)
            divs.append(n//i)
    divs = sorted(list(set(divs)))
    del divs[-1]
    sumdivs = 0
    for i in divs:
        sumdivs += i
    if sumdivs == n:
        return 0
    elif sumdivs < n:
        return -1
    elif sumdivs > n:
        return 1

abundants = []
upperlimit = 28123

for i in range(1, upperlimit):
    if perfectNum(i) == 1:
        abundants.append(i)

doubleabundants = list(abundants)
twoabundants = []
for i in abundants:
    for j in doubleabundants:
        if i+j < upperlimit:
            twoabundants.append(i+j)
    del doubleabundants[0]

unique = sorted(list(set(twoabundants)))
maxsum = sum(range(1, upperlimit))
print(maxsum - sum(unique))
