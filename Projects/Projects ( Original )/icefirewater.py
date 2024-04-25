import random

# global variable 
player_score = 0
bot_score = 0
max_score = 3


# Main game function
def main():

    # Game skills
    skills = [ 'ice' , 'fire' , 'water' ]

    # Player choice
    player_input_skill = input(f"{skills} \n Pick : ")
    print(f"'\n'Player : {player_input_skill}")

    while player_input_skill not in skills:
        print("Invalid pick, pick again!" "\n")
        player_input_skill = input(f"{skills} \n Pick : ")

    # Bot choice
    computer_input_skill = random.choice(skills)
    print(f"Computer : {computer_input_skill}" ,"\n")
    
    if player_input_skill == computer_input_skill:
        return "draw"

    if player_input_skill == "fire":
        if computer_input_skill == "water":
            return "player"
        if computer_input_skill == "ice":
            return "bot"
    
    elif player_input_skill == "ice":
        if computer_input_skill == "water":
            return "player"
        if computer_input_skill == "fire":
            return "bot"
    
    elif player_input_skill == "water":
        if computer_input_skill == "ice":
            return "bot"
        if computer_input_skill == "fire":
            return "player"
        
user_input = input("Play? (Y/N) \n> ").upper()


while user_input == "Y":
        print("\n")
        winner = main()
        print(f"Winner : {winner}" "\n")

        if winner == "draw":
                player_score += 0.5
                bot_score += 0.5
                print(f"Player score : {player_score}" )
                print(f"Bot score : {bot_score}" "\n")


        elif winner == "player":
                player_score += 1
                print(f"Player score : {player_score}" )
                print(f"Bot score : {bot_score}" "\n")

        elif winner == "bot":
                bot_score += 1
                print(f"Player score : {player_score}" )
                print(f"Bot score : {bot_score}" "\n")
        
        if player_score >= max_score:
            print("Player wins!")
            break
        if bot_score >= max_score:
            print("Bot wins!")
            break
        

