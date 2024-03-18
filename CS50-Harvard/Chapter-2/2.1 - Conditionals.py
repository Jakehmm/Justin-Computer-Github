'''

> : 

>= : 

< :

<= :

== :

!= : 

'''
import math

def square_divide(squared_value,divided_value_square) -> int:
    if squared_value < divided_value_square:
        raise ValueError ("Squared value cannot be less than divided value")
    if squared_value == divided_value_square:
        raise ValueError("Cannot be equal")
    return squared_value **2 / divided_value_square

x = int(input("Input x: "))
y = int(input("Input y: "))
print(f"Your final value is {square_divide(x,y)}")

def squareroot(squared_value,divided_value_square) -> int:
    return math.sqrt(square_divide(squared_value,divided_value_square))

print(squareroot(x,y))

def all(squared_value,divided_value_square) -> int:
    return squareroot(squared_value,divided_value_square) + (square_divide(squared_value,divided_value_square))
print(all(x,y))