import random

# Deck arrangements
empty_deck = []

# Full deck
suits = ['Heart' , 'Spade' , 'Diamond' , 'Club']
number_cards = ['Ace', 'Two', 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight', 'Nine' , 'Ten']
face_cards = ['Jack', 'Queen', 'King']


# Tic-Tac-Toe board
board = [' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ' , ' ']
DemoBoard = ['0','1','2','3','4','5','6','7','8']



# Putting cards into empty_deck
for numcards in number_cards:
    for typecard in suits:
        empty_deck.append(numcards +  " of " + typecard)

for faccards in face_cards:
    for typecard in suits:
        empty_deck.append(faccards + " of " + typecard)
   

# Process of printing Tic-Tac-Toe board
def printBoard(board):
    print(f"{board[0]} |  {board[1]} | {board[2]}")
    print(f"{board[3]} |  {board[4]} | {board[5]}")
    print(f"{board[6]} |  {board[7]} | {board[8]}")




    

def player_value_of_cards(player_cards):
    card_value = {'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':20, 'Queen':30, 'King':40}
    player_score = 0

    
    for cards in player_cards:
        player_card = cards.split(" ")[0]
        player_score += card_value.get(player_card,0)
    
    return player_score
   

def bot_value_of_cards(bot_cards):
    card_value = {'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':20, 'Queen':30, 'King':40}
    bot_score = 0
    for cards in bot_cards:
        bot_card = cards.split(" ")[0]
        bot_score += card_value.get(bot_card,0)
    
    return bot_score
    



def Player_placement(board):
    ask_user_placement = int(input("Enter the digit you want your piece to be placed : "))
    print('\n')
    board[ask_user_placement] = "x"
    return board

def Bot_placement(board):
    computer_placement = random.randint(0,8)
    while board[computer_placement] != " ":
        computer_placement = random.randint(0,8)
    board[computer_placement] = "o"
    return board

        
while True:
    # Players deck
    player_deck = []

    # Auto random choose
    player_first_card = empty_deck[random.randint(0,52)]
    player_second_card = empty_deck[random.randint(0,52)]

    # Adding the cards to player deck
    player_deck.append(player_first_card)
    player_deck.append(player_second_card)

   
    # Bot deck
    bot_deck = []

    # Auto random choose
    bot_first_card = empty_deck[random.randint(1,52)]
    bot_second_card = empty_deck[random.randint(1,52)]

    

    # Adding the cards to player deck
    bot_deck.append(bot_first_card)
    bot_deck.append(bot_second_card)
    

    # Show value of card
    print("\n") # Line Break
    player_hand_value = player_value_of_cards(player_deck)
    bot_hand_value = bot_value_of_cards(bot_deck)
    print(f"Player score: {player_hand_value}")
    print(f"Bot score: {bot_hand_value}")

    # Show demo board
    print("\n") # Line Break
    input("> Press ENTER to start ")
    print("\n")
    print('''Enter DIGITS only''')
    print("\n") # Line Break
    printBoard(DemoBoard)

    # Show player board
    print("\n") # Line Break
    input("> Press ENTER to see your board : ")
    print('\n') # Line break
    print("Player board:")
    printBoard(board)
    print("\n") # Line break

    if player_hand_value > bot_hand_value:
        board = Player_placement(board)
        printBoard(board)
    elif bot_hand_value > player_hand_value:
        board = Bot_placement(board)
        printBoard(board)
    break
    
    
    
