"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divded by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""
#!/usr/bin/python

def primeFactors(n):
    primefactors = []
    i = 2
    while i*i<=n:
        if n%i:
            i += 1
        else:
            n //= i
            primefactors.append(i)
    if n>1:
        primefactors.append(n)
    
    return primefactors

numDivisors = 20
minfactors = {}
for i in range(1, numDivisors+1):
    primefactors = primeFactors(i)
    for key in primefactors:
        val = primefactors.count(key)
        if minfactors.has_key(key):
            if minfactors[key] < val:
                minfactors[key] = val
        else:
            minfactors[key] = val

product = 1
for key, val in minfactors.iteritems():
    product *= (key**val)

print product 
