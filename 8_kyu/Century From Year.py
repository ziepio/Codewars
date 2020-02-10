'''Introduction
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
Hope you enjoy it .. Awaiting for Best Practice Codes

Enjoy Learning !!!'''

def century(year):
    if year % 100 == 0:
        return year / 100
    else:
        return int(year/100)+1


test.assert_equals(century(1705), 18, 'Testing for year 1705')
test.assert_equals(century(1900), 19, 'Testing for year 1900')
test.assert_equals(century(1601), 17, 'Testing for year 1601')
test.assert_equals(century(2000), 20, 'Testing for year 2000')
test.assert_equals(century(356), 4, 'Testing for year 356')
test.assert_equals(century(89), 1, 'Testing for year 89')

'''
Other people's solutions:

1.
def century(year):
    return (year + 99) // 100

2.
import math

def century(year):
    return math.ceil(year / 100)

3.
def century(year):
    return (year - 1) // 100 + 1
'''