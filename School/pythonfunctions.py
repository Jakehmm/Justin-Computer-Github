
#Program 1
'''
while True:
    x = int(input("Enter start range: "))
    y = int(input("Enter end range: "))
    z = int(input("Skips: "))

    if z == 0:
        print("Cannot be determined")

    elif x >= y:
        print("Start range has to be less than end range")

    else:
        print(list(range(x,y,z)))
    break
'''

#Program 2
'''
x = int(input("Enter a number: "))
if x % 2 == 0:
   print("The number you just typed is Even")
else:
   print("The number you just typed is Odd")
'''
import math
#Program 3
'''
set_a = math.fsum([2, 10, 4, 12, 5])
set_b = math.fsum([7, 11, 3 ,4, 2])
print(set_a)
print(set_b)
'''






