'''Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

setAlarm(true, true) -> false setAlarm(false, true) -> false setAlarm(false, false) -> false setAlarm(true, false) -> true

setalarm(true, true) -> false
setalarm(false, true) -> false
setalarm(false, false) -> false
setalarm(true, false) -> true'''

def set_alarm(employed, vacation):
    return employed is True and vacation is False


Test.describe("set_alarm")

Test.it("returns correct result for all input values")
Test.assert_equals(set_alarm(True, True), False, "Fails when input is True, True")
Test.assert_equals(set_alarm(False, True), False, "Fails when input is False, True")
Test.assert_equals(set_alarm(False, False), False, "Fails when input is False, False")
Test.assert_equals(set_alarm(True, False), True, "Fails when input is True, False")

'''
Other people's solutions:

1.
def set_alarm(employed, vacation):
    return employed and not vacation

2.    
def set_alarm(employed, vacation):
    # Your code here
    if employed:
        if vacation:
            return False
        return True
    return False

3.
set_alarm=lambda *a:a==(1,0)
'''