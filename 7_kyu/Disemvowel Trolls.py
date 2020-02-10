'''Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.'''

def disemvowel(string):
    vowels = ('a', 'e', 'i', 'u', 'o', 'A', 'E', 'I', 'O', 'U')
    return ''.join([i for i in string if i not in vowels])


test.assert_equals(disemvowel("This website is for losers LOL!"),
                              "Ths wbst s fr lsrs LL!")

'''
Other people's solutions:

1.
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

2.
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
'''