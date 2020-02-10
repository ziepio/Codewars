'''An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case'''

from collections import OrderedDict

def is_isogram(string):
    s = ''.join(OrderedDict.fromkeys(string.lower()))
    string = string.lower()
    if string == s:
        return True
    else:
        return False


Test.assert_equals(is_isogram("Dermatoglyphics"), True )
Test.assert_equals(is_isogram("isogram"), True )
Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
Test.assert_equals(is_isogram("isIsogram"), False )
Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )

'''
Other people's solutions:

1.
def is_isogram(string):
    return len(string) == len(set(string.lower()))

2.
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
'''