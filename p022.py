#!/usr/bin/env python

"""
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3+15+12+9+14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938*53 = 49714.

What is the total of all the name scores in the file?
"""

names = open('p022_names.txt', 'r')
strNames = names.read()
names.close()
strNames = strNames.replace("\"", "")
strNames = strNames.replace(",", " ")
listNames = strNames.split()
listNames.sort()

totalscore = 0
for name in listNames:
    value = 0
    for char in name:
        value += ord(char)-64
    totalscore += (listNames.index(name)+1)*value

print(totalscore)
