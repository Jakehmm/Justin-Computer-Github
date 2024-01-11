# import math option for doing math, no need to be explained
import math
# while True + break statement helps the code run in a loop after choosing the options, same as the picture
while True:
    # Option with int for choosing the number of options shown
    option = int (input('''Options:
        1. Arc Length
        2. Lens Equation
        3. Sum of Numbers
        4. Exit
        Enter the number of your choice: ''', ))
    # One important thing about this code is the indentations, the calculation won't run if they're not in the same line of code 
    if option == 1:
        x = int(input("Enter the radius: ", ))
        y = int(input("Enter the angle in degrees: ", ))
        # formulas
        print("Arc Length:", (2*math.pi*x)*(y/360)) 
    if option == 2:
        x = int(input("Enter the Focal Length: ", ))
        y = int(input("Enter the Object Distance: ", ))
        if (1/x) - (1/y) == 0:
            print("No image is formed")
        else:
            b = 1 / ((1/x) - (1/y))
            print("Image Distance:", b)
    if option == 3:
        x = int(input("Enter a positive integer: ", ))
        y = 0
        for i in range(x + 1):
            y = y + i
        print("Sum of Numbers: ", y)

    if option == 4:
        print("Come back next time!")
        break
    # break helps end the loop
