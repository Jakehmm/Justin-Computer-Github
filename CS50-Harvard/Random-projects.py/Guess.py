import random

# Random number to let user guess
guess_number = random.randint(1, 101)
guess_tries = 1

# Ask user for guess
user_input = int(input("Guess a number: "))

# while user input != to guess, keep looping
while user_input != guess_number:
    
    # if input less than 43 keep loop and print "Higher"
    if user_input < guess_number: 
        print("You've guessed wrong")
        print("Higher!")
       
    # if input greater than 43 keep loop and print "Lower"
    elif user_input > guess_number:
        print("You've guessed wrong")
        print("Lower!")
    
    guess_tries += 1
    # Keep asking user for input if guessed wrong
    user_input = int(input("Guess a number: "))
    
# Out of loop if guessed right
print(f"You've guessed right, it took you {guess_tries} tries!")
  