import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
Demoboard = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

def printBoard(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# User placement
def User_placement(board):
    ask_user_for_placement = int(input("> "))
    print("You have placed your piece at the spot", ask_user_for_placement)
    board[ask_user_for_placement] = "x"
    return board

# Bot placement
def Bot_placement(board):
    computer_placement = random.randint(0,8)
    while board[computer_placement] != " ":
        computer_placement = random.randint(0,8)
    board[computer_placement] = "o"
    return board


# Check who wins
def Win(board):

    # Horizontal lines
    if board[0] == board[1] == board[2] != " ":
        if board[0] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
    if board[3] == board[4] == board[5] != " ":
        if board[3] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
    if board[6] == board[7] == board[8] != " ":
        if board[6] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
    
    # Diagonal lines
    if board[0] == board[4] == board[8] != " ":
        if board[0] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
    if board[2] == board[4] == board[6] != " ":
        if board[2] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
    
    # Vertical lines
    if board[0] == board[3] == board[6] != " ":
        if board[0] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
    if board[1] == board[4] == board[7] != " ":
        if board[1] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
    if board[2] == board[5] == board[8] != " ":
        if board[2] == "x":
            print("Player 'x' has won!")
        else:
            print("Player 'o' has won! ")
        
    return board

while True:

    # Tutorial area : 
    print("\n") # Line break
    print('''You are only allowed to enter INTEGER : ''') # Rule
    printBoard(Demoboard) # Prints the demo board

    # Players board
    print("\n") # Line break
    print('''Please follow the rules!
Your Board : ''')
    printBoard(board)
    print("\n") # Line break

    # Player's placement
    board = User_placement(board) # Updates the list
    print("\n") # Line break
    printBoard(board) # Prints the update list and board format
    
    print("\n") # Line break
    input("> Press enter to see bot's placement ") # Await for bot's placement

    # Bot's placement
    board = Bot_placement(board) # Updates the list
    print("\n") # Line break
    printBoard(board) # Prints the update list and board format
    print("\n") # Line break

    # Player's placement 2
    board = User_placement(board) # Updates the list
    print("\n") # Line break
    printBoard(board) # Prints the update list and board format
    
    print("\n") # Line break
    input("> Press enter to see bot's placement ") # Await for bot's placement

    # Bot's placement 2
    board = Bot_placement(board) # Updates the list
    print("\n") # Line break
    printBoard(board) # Prints the update list and board format
    print("\n") # Line break

    # Player's placement 3
    board = User_placement(board) # Updates the list
    print("\n") # Line break
    printBoard(board) # Prints the update list and board format
    
    print("\n") # Line break
    input("> Press enter to see bot's placement ") # Await for bot's placement

    # Bot's placement 3
    board = Bot_placement(board) # Updates the list
    print("\n") # Line break
    printBoard(board) # Prints the update list and board format
    print("\n") # Line break

    input("> Press enter to check who has won ")
    Win(board)
    break