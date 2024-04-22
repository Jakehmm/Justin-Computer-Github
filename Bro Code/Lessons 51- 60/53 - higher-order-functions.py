# Higher Order Function = a function that either:
#                         1. Accepts a function as an argument
#                         or
#                         2. returns a function
#                        (In python, functions are also treated as objects)


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)

# the `hello` function is called, then we passed in the function 
# loud to the hello function, so text = loud("Hello") , now it
# will return upper case, return it back to the `text` variable
# and we print it

def divisior(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisior(2)
print(divide(10))