'''
Here's how you can use the input() function
.... Think of it as if your making the program ask you a question,
and you can input.
'''


input("1: What's your name? ") 

'''
Output : Nothing

 After testing the code, it will only show the output : "What's your name? "
 If you enter something like, "Justin"
 The program won't respond, this is where variables come in place.
'''

###################################### 

'''
Variable is just a container for value, in programming you don't usually
want your variables typically always x and y, the code inside the variable
should almost be related to the variable name. 

In this case, the variable name is "name", so we could do something like :
'''

name = input("2: What's your name? ")

'''

Output : Nothing

--- Here the function and data is mainly about asking a person's name
So you could basically name it "name" making it more 
specific and descriptive ---

The "=" sign here doesn't mean its "equal" but more of assigning 
a value 
'''
########################################

name_example = input("3: What's your name? ")
print("Hello, (name_example)")

'''
Output : Hello, (name_example)

So why doesn't it work? This is due to the fact it is not string"ed", 
inside the print function, when you hear the word "String", naturally it's 
something like "connecting".
'''

###################
strangers_name = input("4: What's your name? ")
print(strangers_name)

'''
Output : (What you inputed)

In this case we're assigning a variable to the print function,
but it is not string"ed, we're essentially just assigning.
'''

plus_name = input("5: What's your name? ")
print("Hello, " + name)

'''
Output: Hello, (What you inputed)

Here you have a "+" sign, it doesn't mean add essentially like math,
but it's more of combining the single variable.

Note : ("Hello + name") is not the same as the example above, it's essentially
the whole thing.
'''




person_name = input("6: What's your name? ")
print("Hello,", (person_name))

'''
Output : Hello, (What you inputed)

So this time why did it work?
Essentially we are using the "comma : , " to separate the two arguments 
that are going to be printed, "Hello" will definitely be printed, but 
"person_name" on the other hand is on its own. 

Even without the parenthesis on the variable "person_name", it would still 
work cause it's essentially alone.
'''

