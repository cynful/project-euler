"""
Largest product in a series
Problem 8

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 * 9 * 8 * 9 = 5832

Find the thirteen adjacent digits in the 1000-digit number that have the 
greatest product. What is the value of this product?
"""
#!/usr/bin/python

str1000digit = ''
with open('p008_1000digit.txt') as file1000digit:
    for line in file1000digit:
        str1000digit += line.strip()

consecutive = []
maxadjacent = 13
largeProd = 0
i = 0
j = 0
while i < 1000:
    if i+maxadjacent < 1000:
        for j in range(0, maxadjacent):
            if str1000digit[i+j] != "0":
                consecutive.append(int(str1000digit[i+j]))
            else:
                consecutive = []
                i += j
                break
        if len(consecutive) == maxadjacent:
            prod = 1
            for n in consecutive:
                prod *= n
            if prod > largeProd:
                largeProd = prod
    consecutive = []
    i += 1

print largeProd  
