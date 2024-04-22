# lambda function = function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression
# ( think of it as a shortcut )
# (useful if needed for a short period of time,  throw-away)

# lambda paramater:expression

import math

'''
def double(x):
    return x * 2

print(double(5))
'''

double = lambda x: x*2
multiply = lambda x,y: x *y
add = lambda x, y, z: x + y + z

print(double(5))
print(multiply(5,5))
print(add(5,5,5))


full_name = lambda first_name, last_name, middle_name: first_name + " " + middle_name + " " + last_name
print(full_name("Jake", "Zhang" , "Jiekai"))

age_check = lambda age: True if age>= 18 else False
print(age_check(12))
print(age_check(18))