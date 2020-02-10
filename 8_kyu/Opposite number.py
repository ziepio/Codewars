'''Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34'''

def opposite(number):
  return number * (-1)


test.assert_equals(opposite(1),-1)

'''
Other people's solutions:

1.
def opposite(number):
    return –number

2.
from operator import neg as opposite
opposite = lambda x: -x
'''