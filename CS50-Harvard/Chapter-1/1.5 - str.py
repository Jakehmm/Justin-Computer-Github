'''
Here we'll be introducing strings and things we can do to a string 

( fstring ) - This a special function that strings variables together
( strip ) - This is for removing white space
'''


name = (input("Enter your name: "))
name = name.strip()
x = (f"Welcome, {name}")
print(x)
           
