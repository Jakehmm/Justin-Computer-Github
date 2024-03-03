'''
def hello(to):
    print("Hello,", to)

hello()
name = input("What's your name: ")
hello(name)
'''

'''
We are basically making a function that operates something for us
'''

'''
def thanks(to="You"):
    print("Thanks to " + to, ", you made my day")

thanks()
name = input("Your name : ")
thanks(name)
'''

'''
You could also put a value in your argument
and you have to call your function
'''


'''
def numbers(q="Please input numbers: "):
    print(q)
    

numbers()
x = int(input("Enter a digit: "))

y = int(input("Enter another digit: "))

def square(n):
    return n*n
print(square (x)+ square(y))
'''

def numbers(num="Please input an number :) "):
    print(num)
    x = int(input("Enter a digit: "))
    y = int(input("Enter another digit: "))
    print("x divided by y is", divide(x,y))
    

def divide(q, p):
    return q // p


numbers()
