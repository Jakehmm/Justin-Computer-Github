import random

empty_deck_of_cards = []
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
dealer_hand = []
player_hand = []

for i in suits:
    for j in cards:
        empty_deck_of_cards.append(j + " of " + i)

print(empty_deck_of_cards)
print(len(empty_deck_of_cards))

def deal_card(player):
    rand_card = random.randint(0, len(empty_deck_of_cards))
    print(empty_deck_of_cards[rand_card])
    player.append(empty_deck_of_cards[rand_card])
    del empty_deck_of_cards[rand_card]
    print(empty_deck_of_cards[rand_card])

deal_card(dealer_hand)
print(empty_deck_of_cards)