'''Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.'''

def bool_to_word(boolean):
    if boolean is True:
        return 'Yes'
    else:
        return 'No'


Test.assert_equals(bool_to_word(True), 'Yes')
Test.assert_equals(bool_to_word(False), 'No')

'''
Other people's solutions:

1.
def bool_to_word(bool):
    return "Yes" if bool else "No"

2.
def bool_to_word(bool):
    return ['No', 'Yes'][bool]

3.
bool_to_word = {True: 'Yes', False: 'No'}.get
'''