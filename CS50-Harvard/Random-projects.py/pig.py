import random

# Defining value of the roll
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

# Keep asking the user until get int
while True:
    players = input("Enter number of player ( 2 - 5 ) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("Must be between 2 - 5 players.")
    else:   
        print("Invalid, try again")

max_score = 50

# 0 Individual scores for each amount of players
player_scores = [0 for _ in range(players)]
print(player_scores)


while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break

            else:
                current_score += value
                print("You rolled a:" , value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
print(player_scores)
