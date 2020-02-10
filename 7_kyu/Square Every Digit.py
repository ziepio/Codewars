'''Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer'''

def square_digits(num):
    num_str = [int(i) for i in str(num)]
    w = list(map(lambda x: x**2, num_str))
    return int(''.join([str(i) for i in w]))


test.assert_equals(square_digits(9119), 811181)

'''
Other people's solutions:

1.
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

2.
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
'''