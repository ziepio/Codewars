'''You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.'''

def positive_sum(arr):
    not_negative = []
    for i in arr:
        if i >= 0:
            not_negative.append(i)
    return sum(not_negative)


Test.describe("positive_sum")

Test.it("works for some examples")
Test.assert_equals(positive_sum([1,2,3,4,5]),15)
Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

Test.it("returns 0 when array is empty")
Test.assert_equals(positive_sum([]),0)

Test.it("returns 0 when all elements are negative")
Test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

'''
Other people's solutions:

1.
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

2.
def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

3.
def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))
'''