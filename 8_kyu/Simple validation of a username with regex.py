'''Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).'''

import re

def validate_usr(username):
    return bool(re.match(r'[a-z0-9_]{4,16}(?=$)', username))


Test.assert_equals(validate_usr('asddsa'), True)
Test.assert_equals(validate_usr('a'), False)
Test.assert_equals(validate_usr('Hass'), False)
Test.assert_equals(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
Test.assert_equals(validate_usr(''), False)
Test.assert_equals(validate_usr('____'), True)
Test.assert_equals(validate_usr('012'), False)
Test.assert_equals(validate_usr('p1pp1'), True)
Test.assert_equals(validate_usr('asd43 34'), False)
Test.assert_equals(validate_usr('asd43_34'), True)

'''
Other people's solutions:

1.
import re

def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))
'''