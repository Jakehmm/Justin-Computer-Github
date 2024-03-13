'''

> : 

>= : 

< :

<= :

== :

!= : 

'''

def divide_square(to_square,to_divide) -> int:
    if to_divide >= to_square:
        raise ValueError("Try a lower number.")
    if to_divide == to_square:
        raise ValueError("No equivalent numbers, sorry")
    return to_square **2 / to_divide

square_value = int(input("Input a number you want it to be squared: "))
divide_value = int(input("Input the number you want to divide from the squared number: "))


result = divide_square(square_value,divide_value)
print(result)