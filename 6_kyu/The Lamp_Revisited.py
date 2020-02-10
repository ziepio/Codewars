'''Define a class called Lamp. It will have a string attribute for color and boolean attribute, on, that will refer to whether the lamp is on or not. Define your class constructor with a parameter for color and assign on as false on initialize.

Give the lamp an instance method called toggle_switch that will switch the value of the on attribute.

Define another instance method called state that will return "The lamp is on." if it's on and "The lamp is off." otherwise.'''

class Lamp:

    def __init__(self, color, on=False):
        self.color = color
        self.on = on

    def toggle_switch(self):
        if self.on is False:
            self.on = True
        elif self.on is True:
            self.on = False

    def state(self):
        if self.on:
            return 'The lamp is on.'
        else:
            return 'The lamp is off.'


my_lamp = Lamp("Blue")
Test.assert_equals(my_lamp.color, "Blue")
Test.assert_equals(my_lamp.on, False)
Test.assert_equals(my_lamp.state(), "The lamp is off.")
# now switch it on
my_lamp.toggle_switch()
Test.assert_equals(my_lamp.state(), "The lamp is on.")

'''
Other people's solutions:

1.
class Lamp(object):
    def __init__(self, color=None, on=False):
        self.color = color
        self.on = on
    
    def toggle_switch(self):
        self.on = not self.on
        
    def state(self):
        if self.on: s = 'on'
        else: s = 'off'
        return f'The lamp is {s}.'
        
2.
class Lamp:
    def __init__(self, s):
        self.color = s
        self.on = 0
    
    def toggle_switch(self):
        self.on ^= 1
    
    def state(self):
        return f"The lamp is o{'fnf'[self.on::2]}."
        
3.
class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = False
    def toggle_switch(self):
        self.on = not self.on
    def state(self):
        return "The lamp is on." if self.on else "The lamp is off."
'''