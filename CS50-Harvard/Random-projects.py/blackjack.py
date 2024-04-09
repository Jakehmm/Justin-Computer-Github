
# 21  - Trying to get as close to 21 as possible without going over vs the dealer


import random

# Making the decks 

empty_deck = []

suits = ['Hearts' , 'Spades' , 'Diamonds' , 'Clubs']
number_cards = ['Ace' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six', 'Seven' , 'Eight', 'Nine' ,'Ten']
face_cards = ['Jack' , 'Queen' , 'King']

for suit in suits:
    for numbered_cards in number_cards:
        empty_deck.append(numbered_cards + ' of ' + suit)

for suit in suits:
    for face_card in face_cards:
        empty_deck.append(face_card + ' of ' + suit)

random.shuffle(empty_deck)
print(empty_deck)


def main():
    print('''
Rules of Blackjack 21 - 1v1
          
- If player or dealer goes over 21 (lose)
- If player or dealer gets exactly 21 (auto-win)
- Dealer will have one card shown, one card hidden
- To continue drawing click (d)
          
''')

main()
# Define a function when a player gets card
def value_card(player_cards):
    player_cards = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine":9, "Ten":10, "Jack": 10, "Queen": 10, "King" : 10 }
    



first_hand = empty_deck[random.randint(0,52)]
second_hand = empty_deck[random.randint(0,52)]


player_cards = []
player_one_cards =  value_card(player_cards)

# Main game loop 
while True:

    user_input = input('''
Play? (y / n)
> ''')
    
    if user_input[0] == 'y':
        print('''Dealer : Alrighty, let's start the game shall we?
              
*Dealer distributes two cards*
              
Your cards are: ''')
        
    player_cards.append(first_hand)
    player_cards.append(second_hand)
    print(player_cards)

    user_input_hd = input('''
'Hit' or 'Draw'?
> ''')
    if user_input_hd[0].lower() == 'd': 
        player_cards.append(empty_deck[random.randint(0,52)])

    elif user_input_hd[0].lower() == 'h':
