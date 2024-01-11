# Without making new line input
x = int(input("Enter first side: "))
y = int(input("Enter second side: "))
z = int(input("Enter third side: "))

# If x = y = z then it will return
if(x == y == z):
    print("Equilateral")

# If one of the variables are equal to each other it will return
elif(x == y or y == z or x == z):
     print("Isosceles")

# If none sides are equal to each other it will return
elif(x != y != z):
     print("Obtuse")
# If doesn't input a number but a word, it will return
else:
     print("Try Again")
     