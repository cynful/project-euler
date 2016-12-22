"""
Maximum path sum 1
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with a
triangle containing one-hundred rows; it cannot be solved by brute force,
and requires a clever method! ;o)
"""
#!/usr/bin/local

pyrlist = []
with open('p018_pyramid.txt') as filepyramid:
    for line in filepyramid:
        level = map(int, line.split())
        pyrlist.append(level)

pyrsize = len(pyrlist)
for i in range(pyrsize-1, 0, -1):
    deletelvl = pyrlist[i]
    replacelvl = pyrlist[i-1]
    newlvl = []
    for j in range(0, len(replacelvl)):
        left = replacelvl[j] + deletelvl[j]
        right = replacelvl[j] + deletelvl[j+1]
        newlvl.append(max(left,right))
    pyrlist.pop()
    pyrlist.pop()
    pyrlist.append(newlvl)

print pyrlist[0][0]
