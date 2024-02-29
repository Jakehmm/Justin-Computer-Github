'''
Here we'll be introducing strings and functions we can do to a string 

( fstring ) - This a special function that strings variables together
( strip ) - This is for removing white space
( capitalize) - Capitalizing the first letter
'''

# Note: The variable "name" is also a string 
name = (input("Enter your name: "))

# This removes whitespace from str ( You could also chain the functions)
name = name.strip()


# This is to capitalize the first letter ONLY
name = name.capitalize()

# This is to capitilize the FULL INPUT
name = name.title()

'''
as title() suggest, think of a book, we usually 
capitalize the title right?
'''

x = (f"Welcome, {name}")
print(x)

''' 
We can see here "x" and "name" is a string, 
and inside the value of x I string-ed it with "name" using the f string
{} - The curly brackets indicate it is added 
'''


# Here is a fast and nice way to write your code efficiently
user_name = input("What's your name? ").strip().title()
q = (f"Hello, {user_name}")
print(q)