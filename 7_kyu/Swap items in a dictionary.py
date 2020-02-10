'''In this kata, you will take the keys and values of a dictionary and swap them around.

You will be given a dictionary, and then you will want to return a dictionary with the old values as the keys, and list the old keys as values under their original keys.

For example, given the dictionary: {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'},

you should return: {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}

Notes:
The dictionary given will only contain strings
The dictionary given will not be empty
You do not have to sort the items in the lists'''

def switch_dict(dic):
    new_dic = {}
    for key, value in dic.items():
        if value not in new_dic.keys():
            new_dic[value] = [key]
        else:
            new_dic.setdefault(value, []).append(key)
    return new_dic


before = {
          'Ice': 'Cream',
          'Age': '21',
          'Light': 'Cream',
          'Double': 'Cream'
          }

expected_ans = {
                'Cream': ['Ice', 'Double', 'Light'],
                '21': ['Age']
                }


usr_ans = switch_dict(before)

# Sort lists inside dict
usr_ans = {k: sorted(usr_ans[k]) for k in usr_ans}
expected_ans = {k: sorted(expected_ans[k]) for k in expected_ans}

test.describe('Basic tests')

test.it('Sample case')
test.assert_equals(usr_ans, expected_ans)

'''
Other people's solutions:

1.
def switch_dict(dic):
    result = {}
    for key, value in dic.items():
        result.setdefault(value, []).append(key)
    return result

2.
from collections import defaultdict

def switch_dict(dct):
    revDct = defaultdict(list)
    for k,v in dct.items(): revDct[v].append(k)
    return revDct

3.
switch_dict = lambda d: {v: [k for k in d.keys() if d.get(k) == v] for v in d.values()}
'''