'''Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice'''

def duplicate_count(text):
    t_list = [i.lower() for i in text]
    sorted_list = t_list.sort()
    print(t_list)
    l = []
    for i in range(1, len(t_list)):
        if t_list[i-1] == t_list[i]:
            if t_list[i] not in l:
                l.append(t_list[i])
    print(f'Lisa duplikatów: {l}')
    print(len(l))
    return len(l)


test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)

'''
Other people's solutions:

1.
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
  
2.
def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

3.
from collections import Counter

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)
    
4.
def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count
'''