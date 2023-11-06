# Create a blackjack program 

# Step1: Create a deal_card() function that selects a random card from the stack 
import random

def deal_card():
    """
    Randomly selects a card from a stack of cards. 
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Step 2: Deal the user and computer 2 cards each using the deal_card function created above.

user_cards = []
computer_cards = []
game_on = True

# Use for loop to run it twice: 

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print("The cards are:")
print(user_cards)
print(computer_cards)

# Create a calculate_score() function that takes a list of cards and returns the total score.
# Inside the calculate_score() function, check to see whether it is a 2-hand card and the total is 21
# If that is the case, return 0 - meanng this is a blackjack

def calculate_score(card_list):
    sum_cards = 0
    if len(card_list) == 2 and sum(card_list) == 21:
        sum_cards = 0
    elif 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    sum_cards = sum(card_list)
    return sum_cards


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print("Total scores")
print(user_score)
print(computer_score)

# Call the calculate score function and if the user has 0 or if the score is over 21, then the game ends'


