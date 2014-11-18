"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""
#!/usr/bin/python

palindrome = 0
for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        prod = i*j
        s = str(prod)
        if s == s[::-1] and prod > palindrome:
            palindrome = prod
print palindrome
