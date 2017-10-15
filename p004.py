#!/usr/bin/env python

"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""

minDigits = 100
maxDigits = 999
palindrome = 0
for i in range(minDigits, maxDigits+1):
    for j in range(minDigits, maxDigits+1):
        prod = i*j
        s = str(prod)
        if s == s[::-1] and prod > palindrome:
            palindrome = prod

print(palindrome)
