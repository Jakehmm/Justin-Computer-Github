def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    

user_input = input("Player 1 Throw: ")
user_input_two =  input("Player 2 Throw: ")

print(rps(user_input,user_input_two))