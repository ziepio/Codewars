'''Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.'''

def maps(a):
    return list(map(lambda a:a*2, a))


test.describe("Sample tests")
test.assert_equals(maps([1, 2, 3]), [2, 4, 6])
test.assert_equals(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
test.assert_equals(maps([]), [])

'''
Other people's solutions:

1.
def maps(a):
    return [2 * x for x in a]
'''