'''Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5'''

def litres(time):
    #return round(time*0.5)
    if time >= 2:
        return int(time * 0.5)
    else:
        return 0


test.describe('Fixed tests')
test.it('Tests')
test.assert_equals(litres(2), 1, 'should return 1 litre');
test.assert_equals(litres(1.4), 0, 'should return 0 litres');
test.assert_equals(litres(12.3), 6, 'should return 6 litres');
test.assert_equals(litres(0.82), 0, 'should return 0 litres');
test.assert_equals(litres(11.8), 5, 'should return 5 litres');
test.assert_equals(litres(1787), 893, 'should return 893 litres');
test.assert_equals(litres(0), 0, 'should return 0 litres');

'''
Other people's solutions:
                            # int zaokrągla w dół w zakresie 0-0.9
1.
def litres(time):
    return time // 2		#  znak // określa zmienną jako int, int j.w.

2.
def litres(time):
    return int(time/2)

3.
def litres(time):
    return int(time*0.5)
'''