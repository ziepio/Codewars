'''Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.'''

def square_sum(numbers):
    return sum(map(lambda a: a*a, numbers))


Test.expect(square_sum([1,2]), 'squareSum did not return a value')
Test.assert_equals(square_sum([1,2]), 5)
Test.assert_equals(square_sum([0, 3, 4, 5]), 50)

'''
Other people's solutions:

1.
def square_sum(numbers):
    return sum(x * x for x in numbers)

2.
def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))
'''