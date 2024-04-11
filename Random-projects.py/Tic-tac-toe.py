import random

board_placement= [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
DemoBoard = ['1', '2' , '3' , '4' , '5', '6' , '7' , '8' , '9']
      
        



def printBoard(board):
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print(f"{board[6]} | {board[7]} | {board[8]}")

def UserMove(board_placement):
    ask_user_placement = int(input("Place your piece : "))
    board_placement[ask_user_placement - 1] = "x"
    return board_placement

def ComputerMove(board_placement):
    computer_placement = random.randint(0,8)
    while board_placement[computer_placement] != " ":
        computer_placement = random.randint(0,8)
    board_placement[computer_placement] = "o"
    return board_placement

def CheckForWin(board_placement):

    # Horizontal Lines
    if board_placement[0] == board_placement[1] == board_placement[2] != " ":
        if board_placement[0] == "x":
            print("Player 'x' has won!")
        else:
            print("Bot has won!")

    elif board_placement[3] == board_placement[4] == board_placement[5] != " ":
         if board_placement[3] == "x":
            print("Player 'x' has won!")
         else:
            print("Bot has won!")
    elif board_placement[6] == board_placement[7] == board_placement[8] != " ":
        if board_placement[6] == "x":
            print("Player 'x' has won!")
        else:
            print("Bot has won!")
    # Diagonal Lines
    elif board_placement[0] == board_placement[4] == board_placement[8] != " ":
         if board_placement[0] == "x":
            print("Player 'x' has won!")
         else:
            print("Bot has won!")
    elif board_placement[6] == board_placement[4] == board_placement[2] != " ":
        if board_placement[6] == "x":
            print("Player 'x' has won!")
        else:
            print("Bot has won!")

    # Vertical Lines
    elif board_placement[0] == board_placement[3] == board_placement[6] != " ":
        if board_placement[0] == "x":
            print("Player 'x' has won!")
        else:
            print("Bot has won!")
    elif board_placement[1] == board_placement[4] == board_placement[7] != " ":
        if board_placement[1] == "x":
            print("Player 'x' has won!")
        else:
            print("Bot has won!")
    elif board_placement[2] == board_placement[5] == board_placement[8] != " ":
        if board_placement[2] == "x":
            print("Player 'x' has won!")
        else:
            print("Bot has won!")

while True: 

    #1
    print("\n""Demo board : ", "\n")
    printBoard(DemoBoard) # Prints the demo board

    #2
    print("\n""Your board : ", "\n")
    printBoard(board_placement) # Prints the board

    #3 
    print("\n") # Space
    board_placement = UserMove(board_placement) # Updates the list with what user inputed and calls the function
    print("\n") # Space
    printBoard(board_placement) # Print the board

    #4 
    board_placement = ComputerMove(board_placement) # Updates the list of what the computer did and calls the function
    print("\n") # Space
    printBoard(board_placement) # Print the board

    #3.1
    print("\n") # Space
    board_placement = UserMove(board_placement) # Updates the list with what user inputed and calls the function
    print("\n") # Space
    printBoard(board_placement) # Print the board

    #4.1 
    board_placement = ComputerMove(board_placement) # Updates the list of what the computer did and calls the function
    print("\n") # Space
    printBoard(board_placement) # Print the board

    #3.2
    print("\n") # Space
    board_placement = UserMove(board_placement) # Updates the list with what user inputed and calls the function
    print("\n") # Space
    printBoard(board_placement) # Print the board

    #4.2
    board_placement = ComputerMove(board_placement) # Updates the list of what the computer did and calls the function
    print("\n") # Space
    printBoard(board_placement) # Print the board

    CheckForWin(board_placement)
    

    break