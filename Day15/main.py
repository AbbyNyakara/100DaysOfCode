from art import logo, vs
from data import data
import random

# Define the variables: 

def print_info(account):
    """Takes the account name and returns a formatted version"""
    account_name = account['name']
    account_description = account['description']
    acount_country = account['country']
    return (f"{account_name}, a {account_description} from {acount_country}")


def check_answer(guess, account_a_followers, account_b_followers):
    """Check the guess against the followers for account A and account B and returns
    whether the user got it right. """
    if account_a_followers > account_b_followers:
        return guess == "a"  # This will return true
    else:
        return guess== "b"   # This will return false

# Display the art
print(logo)
score = 0
continue_game = True

account_b = random.choice(data)

# make the game repeatable.
while continue_game:
# Generate a random instagram account from the game data
    

    # Format account data into printable format

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {print_info(account_a)}")
    print(vs)
    print(f"Against B: {print_info(account_b)}")

    # Ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check the user's guess to see whether it's right or wrong.
    ## Check the follower count of each account
    ## use if statement to check whether it's right or wrong
    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']

    # Call the check answer function and pass in the parameters. 
    is_correct = check_answer(guess, follower_count_a, follower_count_b)

    # Give the user feedback on whether they are right or wrong:
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        
    else:
        continue_game = False
        print(f"Thats wrong: Your score: {score}")





# Make the account at position B to be position A
