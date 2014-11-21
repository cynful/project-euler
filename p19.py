"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""
#!/usr/bin/python

import datetime

sundays = 0
sunday = 6
begin = 1901
end = 2000
months = 12
for i in range(begin, end+1):
    for j in range(1, months+1):
        date = datetime.date(i, j, 1)
        if date.weekday() == sunday:
            sundays += 1

print sundays
