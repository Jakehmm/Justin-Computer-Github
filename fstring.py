# using f string
name = input("What's your name? ")
print(f"hello, {name}")

#Removing whitespace from str
name = name.strip()

#Capitalizing user's name (each first letter word)
name = name.title()

#Removing whitespace from str and
#capitalizing each first letter word"
name = name.strip().title()

# using f string to remove whitespace from str
# and capitalizing each letter word
name = input("What's your name? ").strip().title()


print(f"hello, {name}")