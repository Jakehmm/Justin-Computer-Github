
def rpsls(pl1, pl2):
    while True:
        if pl1 == pl2:
            return "Draw!"
        if pl1 == "rock" and pl2 == "lizard":
            print("Player 1 Won!")

        if pl1 == "paper" and pl2 == "rock":
            print("Player 1 Won!")
        if pl1 == "scissors" and pl2 == "lizard":
            print("Player 1 Won!")
        if pl1 == "lizard" and pl2 == "paper":
            print("Player 1 Won!")
        if pl1 == "spock" and pl2 == "rock": 
            break
        else:
            return "Player 2 Won!"
    
    while True:
        if pl1 == "lizard" and pl2 == "scissors":
            return "Player 2 Won!"
        elif pl1 == "spock" and pl2 == "lizard":
            return "Player 2 Won!"
        elif pl1 == "paper" and pl2 == "lizard":
            return "Player 2 Won!"
        elif pl1 == "scissors" and pl2 == "spock":
            return "Player 2 Won!"
        elif pl1 == "rock" and pl2 == "spock":
            return "Player 2 Won!"
        else:
            return "Player 1 Won!"
    

user_input = input("Player 1 Throw: ")
user_input_two =  input("Player 2 Throw: ")

print(rpsls(user_input,user_input_two))