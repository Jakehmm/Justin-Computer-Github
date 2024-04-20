# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*args): # packing into a tuple , can be named any # doesn't need to be arg 
    sum = 0
    # stuff[0] = 1 # doesn't work because it's not mutable 
    args = list(args) # this is mutable
    args[0] = 200
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))