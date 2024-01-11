# import sys provides more function, with this the else would print instead of just using if elif
import sys
try : 
    x = int(input("Enter First Side: "))
    y = int(input("Enter Second Side: "))
    z = int(input("Enter Third Side: "))

# Else return " "
except ValueError:
    print("Type a number instead of alphabet ")
    sys.exit()

# If Value x y z = to each other it will return
if x == y == z :
    print("Equilateral")

#If one value = to one another it will return
elif x == y or y == z or z == x :
    print("Isosceles")

#If none of the value = to another it will return
elif x != y != z :
    print("Obtuse")