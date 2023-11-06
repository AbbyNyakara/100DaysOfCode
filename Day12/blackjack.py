# The following is the list of cards in the deck:
# the cards are not removed from the deck once they are drawn. 
# The jack/Queen/King all count as 10
# The Ace can count as 1 or 11
# All the other cards are just the face value. 
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of blackjack? Type 'y' or 'n' \n").lower()

player_cards = []
computer_cards = []
card_length = len(cards)

def generate_card():
    """
    Generates a random card
    """
    random_index = random.randint(1, card_length-1)
    random_card = cards[random_index]
    return random_card

# Computer_card
computer_cards.append(generate_card())
print(f"The computer's card is {computer_cards}")
# Player card
card_1 = generate_card()
card_2 = generate_card()

if play == 'y':
    # Player card
    card_1 = generate_card()
    card_2 = generate_card()
    player_cards.append(card_1)
    player_cards.append(card_2)
    #print(player_cards)

print(f" Your cards are {player_cards}. Current score is {sum(player_cards)}")

pick_card = input("Type 'y' to get another card, type 'n' to pass: \n")

if pick_card == 'y'.lower():
    new_card = generate_card()
    player_cards.append(new_card)

print(f"Your final hand is: {player_cards}")
computer_cards.append(generate_card())

print(f"The computer's final hand is {computer_cards}")
