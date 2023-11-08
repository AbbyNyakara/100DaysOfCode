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
is_game_over = False

# Use for loop to run it twice: 

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Create a calculate_score() function that takes a list of cards and returns the total score.
# Inside the calculate_score() function, check to see whether it is a 2-hand card and the total is 21
# If that is the case, return 0 - meanng this is a blackjack

def calculate_score(card_list):
    """Takes a list of cards and calculates the score"""
    if len(card_list) == 2 and sum(card_list) == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return(sum(card_list))


while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards are: {user_cards}. Your total score is {user_score}")
    print(f"The computer's first card is {computer_cards[0]}")

    # The game should end if the user score or computer score is 0 and if the user score is over 21
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        draw_card = input("Would you like to draw another card? type 'y' or 'n' \n ")
        if draw_card == 'y'.lower():
            user_cards.append(deal_card())
        else:
            is_game_over = True


# Once the user is done, its time to let the computer play. as long as the score is less than 17, 
# the computer should keep drawing cards
    
while computer_score != 0 or computer_score < 17:
    computer_score.append(deal_card())
    # update the computer score
    computer_score = calculate_score(computer_score)


# Create a function called compare.Pass in the 


