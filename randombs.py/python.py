print("Input the value of each side: ")
A= int(input("First side: "))
B = int(input("Second side: "))
C = int(input("Third side: "))

if A == B == C :
    print(" It is an Equilateral triangle")
elif A == B or B == C or C == A:
    print("It is an Isosceles triangle")
else:
    print("It is an Obtuse triangle")
