# exception = events detected during execution that interrupt the flow of
# a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0")
except ValueError as e:
    print(e)
    print("Enter only numbers! PLEASE!")

except Exception as e:
    print(e)
    print("Something wen't wrong :(")
else:
    print(result)
finally:
    print("FUCKING RETARDED SHIT - This will always execute") 