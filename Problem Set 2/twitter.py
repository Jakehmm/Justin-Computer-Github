# List of vowels
vowels = [ 'a' , 'e' , 'i' , 'o' , 'u']


# Ask user for input
user_input = input(("Input: "))
user_output = 'Output: '

# Removing Vowels
for letter in user_input:
    if letter.lower() not in vowels:
        user_output +=  letter
    print(user_output)

print(user_output)

# loop is going through each letter, if the statement is false, it doesnt print anything

'''
Another solution
'''

# Get user input
answer = input("Input: ")

# Print ouput
print("Ouput: ", end = "")

# Loop through every letter
for letter in answer:

# Check the vowel is in lower case
    if letter.lower() not in [ 'a' , 'e' , 'i' , 'o' , 'u']:

        # Print the letter
        print(letter, end='')

# Print new line
print()

