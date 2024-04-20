import random

choices = ['rock' , 'paper' , 'scissors' ]

player_score = 0
bot_score = 0
max_score = 2

player = None
computer = random.choice(choices)

while player is not choices:
    player_input = input("rock , paper , scissor? \n> ").lower()

    if player_input == computer:
        print("Draw!")
        player_score += 0.5
        bot_score += 0.5
    
    elif player_input == "scissor":
        if computer == "paper":
            print("Player wins!")
            player_score += 1

        if computer == "rock":
            print("Bot wins!")
    
    elif player_input == "rock":
        if computer == "paper":
            print("Bot wins!")

        if computer == "scissor":
            print("Player wins!")
            player_score += 1

    elif player_input == "paper":
        if computer == "rock":
            print("Player wins!")
            player_score += 1

        if computer == "scissor":
            print("Bot wins!")

    if player_score >= max_score:
        break
    print("Player wins!")

    
    
