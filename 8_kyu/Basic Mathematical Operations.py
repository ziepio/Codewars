'''Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples
basic_op('+', 4, 7)         # Output: 11
basic_op('-', 15, 18)       # Output: -3
basic_op('*', 5, 5)         # Output: 25
basic_op('/', 49, 7)        # Output: 7'''

def basic_op(operator, value1, value2):
    if operator is '+':
        return value1 + value2
    elif operator is '-':
        return value1 - value2
    elif operator is '*':
        return value1 * value2
    else:
        return value1 / value2


Test.describe("Basic tests")
Test.assert_equals(basic_op('+', 4, 7), 11)
Test.assert_equals(basic_op('-', 15, 18), -3)
Test.assert_equals(basic_op('*', 5, 5), 25)
Test.assert_equals(basic_op('/', 49, 7), 7)

'''
Other people's solutions:

1.
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')
In simple terms, the eval() method runs the python code (which is passed as an argument) within the program.

The syntax of eval() is:
eval(expression, globals=None, locals=None)

2.
def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)

3.
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))
'''