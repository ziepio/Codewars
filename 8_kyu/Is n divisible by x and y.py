'''Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.

Example:
is_divisible(3,1,3)--> True because 3 is divisible by 1 and 3
is_divisible(12,2,6)--> True because 12 is divisible by 2 and 6
is_divisible(100,5,3)--> False because 100 is not divisible by 3
is_divisible(12,7,5)--> False because 12 is neither divisible by 7 nor 5'''

def is_divisible(n,x,y):
    if n > 0 and n % x == 0 and n % y == 0:
        return True
    else:
        return False


Test.assert_equals(is_divisible(3,3,4),False)
Test.assert_equals(is_divisible(12,3,4),True)
Test.assert_equals(is_divisible(8,3,4),False)
Test.assert_equals(is_divisible(48,3,4),True)

'''
Other people's solutions:

1.
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

2.
def is_divisible(n, x, y):
    return n % x == n % y == 0

3.
def is_divisible(n,x,y):
    return n % x + n % y == 0
'''