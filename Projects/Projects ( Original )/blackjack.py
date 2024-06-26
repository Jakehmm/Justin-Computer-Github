
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



def main():
    print('''
Rules of Blackjack 21 - 1v1
          
- If player or dealer goes over 21 (lose)
- If player or dealer gets exactly 21 (auto-win)
- Dealer will have one card shown, one card hidden
- To draw a card enter (h)''')

main()
# Define a function when a player gets card
# card_values will overwrite card_score ( if they had the same variable name)
def value_card(player_cards,dealer_cards):

    # Card Values
    card_score = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine":9, "Ten":10, "Jack": 10, "Queen": 10, "King" : 10 }
    

    
    player_score = 0
    dealer_score = 0
    for card in player_cards:

        card = card.split(" ")[0] # not commented out
        if card == 'Ace':
            user_input = int(input('''You have an Ace card in your deck, 
Do you want to make your Ace 1 or 11?
> '''))
            if user_input == 1:
                new_card = {'Ace':1}
                card_score.update(new_card)
            elif user_input == 11:
                new_card = {'Ace':11}
                card_score.update(new_card)
        player_score += card_score.get(card, 0)

    for cards in dealer_cards:
        cards = cards.split(" ")[0] # not commented out


        dealer_score += card_score.get(card, 0)
    print(player_score)
    print(dealer_score)

    if player_score > 21: 
        print("Player has lost!")
    elif dealer_score > 21:
        print("Dealer has lost!")
    if player_score == dealer_score:
        print("Draw") 
    elif player_score <= 21 and player_score > dealer_score:
        print("Player has won")
    elif dealer_score <= 21 and dealer_score > player_score:
        print("Dealer has won!")
    

    
    


# Creating players cards
player_cards = []
first_hand = empty_deck[random.randint(0,52)]
second_hand = empty_deck[random.randint(0,52)]

# Dealers cards
dealer_cards = []
dealers_first_hand = empty_deck[random.randint(0,52)]
dealers_second_hand = empty_deck[random.randint(0,52)]



# Main game loop 
while True:

    user_input = input('''
Play? (y / n)
> ''')
    
    if user_input[0] == 'y':
        print('''Dealer : Alrighty, let's start the game shall we?    
                     
*Dealer distributes two cards*
              
Your cards are: ''')
        
    # Player cards   
    player_cards.append(first_hand)
    player_cards.append(second_hand)
    print(player_cards, '\n')

    
    
    # Dealer's card
    dealer_card_decision = random.randint(1,2)
    print('''Dealers hand : ''')
    dealer_cards.append(dealers_first_hand)
    dealer_cards.append(dealers_second_hand)
    print(f"First card : {dealer_cards[0]}, Second card : ", '\n')

    # Decision making
    print('''Dealer is deciding to hit a card or not....''')
    if dealer_card_decision == 1:
        dealer_cards.append(empty_deck[random.randint(0,52)])    
    

    user_input_hd = input('''
'Hit' or 'Stand'?
> ''')
    if user_input_hd[0].lower() == 'h': 
        player_cards.append(empty_deck[random.randint(0,52)])
        print(f"Your new card : {player_cards[2]}, Your deck : {player_cards}" )

    #Transport the value
    hand_value = value_card(player_cards,dealer_cards)

    if user_input_hd[0].lower() == 's':
        print(hand_value)
    
        break # hit/stand break
    break # main game loop break