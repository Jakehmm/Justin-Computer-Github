# Adding Decimals, not the same as Calculator.py 
# Which only adds integers

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

#Rounding off

#round(number[, ndigits])

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x+y)

print (z)

# also can just

# print( x + y )

############################################

# For adding comma

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x+y)

print(f"{z:,}")


########################################################
#Division 2 ways 
# the round( x / y, 3) 
# 3 represents how much u want to round to
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round( x / y, 3)

print(z)

#
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")

#####################################################