'''You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"

#Input
A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#Output
The middle character(s) of the word represented as a string.'''

def get_middle(s):
    x = len(s) // 2

    if len(s) % 2 != 0:
        return s[x]
    else:
        return s[x - 1] + s[x]


Test.assert_equals(get_middle("test"),"es")
Test.assert_equals(get_middle("testing"),"t")
Test.assert_equals(get_middle("middle"),"dd")
Test.assert_equals(get_middle("A"),"A")
Test.assert_equals(get_middle("of"),"of")

'''
Other people's solutions:

1.
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]

2.
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]

3.
import math
def get_middle(s):
    #your code here
    x = len(s)
    y = int(x/2)
    if x%2==0:
        return s[y-1:y+1]
    else:
        return s[y:y+1]

4.
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
'''