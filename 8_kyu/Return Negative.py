'''In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes:

The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.'''

def make_negative( number ):
    if number >= 0:
        return number * -1
    else:
        return number


Test.assert_equals(make_negative(42),-42)

'''
Other people's solutions:

1.
def make_negative( number ):
    return -abs(number)

2.
def make_negative( number ):
    return -number if number>0 else number

3.
def make_negative(number):
    if number >= 0:
        return (0 - number)
    else:
        return numer

4.
def make_negative(n):
    return n if n <= 0 else –n
'''