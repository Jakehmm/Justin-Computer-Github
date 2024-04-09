
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
- To draw a card enter (h)
          
''')

main()
# Define a function when a player gets card
# card_values will overwrite card_score ( if they had the same variable name)
def value_card(card_values,dealers_cards):

    print(card_values)
    card_score = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine":9, "Ten":10, "Jack": 10, "Queen": 10, "King" : 10 }
    score = 0
    for card in card_values:
        card = card.split(" ")[0] # not commented out

        
        print(score)
        score += card_score.get(card, 0)
    if score > 21:
        print(f"You've lost, your score:", score)
    
    if card_values > dealers_cards:
        print("You've lost! Dealer wins!")


    
    


# Creating players cards
first_hand = empty_deck[random.randint(0,52)]
second_hand = empty_deck[random.randint(0,52)]

# Dealers cards
dealer_cards = []
dealers_first_hand = empty_deck[random.randint(0,52)]
dealers_second_hand = empty_deck[random.randint(0,52)]

# Store player card
player_cards = []




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
    print("\n")
    print('''Dealers hand : ''')
    dealer_cards.append(dealers_first_hand)
    dealer_cards.append(dealers_second_hand)
    print(dealer_cards)
    #Transport the value
    

    user_input_hd = input('''
'Hit' or 'Stand'?
> ''')
    if user_input_hd[0].lower() == 'h': 
        player_cards.append(empty_deck[random.randint(0,52)])
        print(f"Your new card : {player_cards[2]}")

    hand_value = value_card(player_cards,dealer_cards)

    if user_input_hd[0].lower() == 's':
        print(hand_value)
    
        break
    break



    