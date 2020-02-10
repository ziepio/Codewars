'''You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)'''

def find_outlier(integers):
    odd = [i for i in integers if i % 2]
    even = [i for i in integers if not i % 2]

    if len(odd) > len(even):
        return even[0]
    return odd[0]


test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

'''
Other people's solutions:

1.
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

2.
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

3.
def find_outlier(integers):
    assert len(integers) >= 3

    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False

4.
def find_outlier(integers):
    even = filter(lambda x: x % 2 == 0, integers)
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]
'''