# + 
# - 
# *
# /
# %

#Integer
#2 Ways - Readable

#if just z = x + y it will just string it
#So use int to make it a integer

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

##########################################

x = int(input("What's x? "))
y = int(input("What's y? "))

print (x + y)


#Squaring using return 
# return pow(n , 2)

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

