"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""
#!/usr/bin/python

numMap = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen',
20: 'twenty',
30: 'thirty',
40: 'forty',
50: 'fifty',
60: 'sixty',
70: 'seventy',
80: 'eighty',
90: 'ninety',
100: 'hundred',
1000: 'thousand',
}

maxcount = 1000
sum = 0
for i in range(1, maxcount+1):
    r = i
    britStd = False
    if r/1000 != 0:
        q = r/1000
        sum += len(numMap[q] + numMap[1000])
        r %= 1000
    if r/100 != 0:
        q = r/100
        sum += len(numMap[q] + numMap[100])
        r %= 100
        if r != 0:
            britStd = True
    if britStd:
        sum += len('and')
    if r/10 >= 2:
        q = r/10
        sum += len(numMap[q*10])
        r %= 10
    if r/10 == 1:
        q = r/10
        r %= 10
        sum += len(numMap[q*10+r])
        r = 0
    if r != 0:
        sum += len(numMap[r])

print sum
