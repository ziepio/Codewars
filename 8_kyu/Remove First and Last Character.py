'''It's pretty straightforward. Your goal is to create a function that removes the first and last characters
of a string. You're given one parameter, the original string. You don't have to worry with strings with less than
two characters.'''

def remove_char(s):
    return s[1:-1]


Test.describe("Tests")
Test.assert_equals(remove_char('eloquent'), 'loquen')
Test.assert_equals(remove_char('country'), 'ountr')
Test.assert_equals(remove_char('person'), 'erso')
Test.assert_equals(remove_char('place'), 'lac')
Test.assert_equals(remove_char('ok'), '')

'''
Other people's solutions:

1.
remove_char=lambda s: s[1:-1]

2.
def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)
'''