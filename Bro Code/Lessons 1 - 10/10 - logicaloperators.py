# Logical operators (and, or, not) = used to check if
# two or more conditional statements are True

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30: # Both conditions must be true, to run
    print("Nice weather innit?")

elif temp < 0 or temp > 30: # One condition must be true, to run
    print("The weather shit innit")

# Not operator will flip it to be True
user_input = input("Do you want the game to be over? (Y / N) ")
if user_input[0].upper() == 'Y':
    game_over = False
elif user_input[0].upper() == 'N':
    game_over = True

while not(game_over):
    print("Well done!")
    break
