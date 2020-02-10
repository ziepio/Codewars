'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.'''

def find_short(s):
    splited_sent = s.split()
    index_list = [len(i) for i in splited_sent]
    l = min(index_list)
    return l # l: shortest word length


test.describe("Basic Tests")
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)

'''
Other people's solutions:

1.
def find_short(s):
    return min(len(x) for x in s.split())
    
2.
def find_short(s):
    return len(min(s.split(' '), key=len))
    
3.
def find_short(s):
    return min(map(len, s.split(' ')))
'''