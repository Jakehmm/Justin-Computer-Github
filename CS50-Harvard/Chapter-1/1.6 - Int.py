'''
Python also support math
int() - integers
float() - decimal point
round() - rounding numberss
'''

# wrong way of doing math without int
'''
x = input("Enter first digit: ")
y = input("Enter second digit: ")
 
z = x + y

print(f"{z} - you should not do this")
'''

'''
This concatenates the string because the "+" symbol is used different in python
'''

# Right way of doing math using int
'''
x = int(input("Enter first digit: "))
y = int(input("Enter second digit: "))

print(f"{x+y} - you should do it like this")

This is what we call nesting functions
'''

# Float and round usage
'''
x = float(input("Input a digit with a decimal: "))
y = float(input("Input another digit with a decimal: "))

z = round(x+y)
print(f"{z:,}")

it might look a bit cryptic, but that's essentially how u add comma's its ok to 
search up google for that fr
'''

# Rounding to what which area of number
'''
x = float(input("Input a digit with a decimal: "))
y = float(input("Input another digit with a decimal: "))

z = round(x/y , 2)
print(z)
'''