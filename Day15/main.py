from art import logo, vs
from data import data
import random

def print_info(account):
    """Takes the account name and returns a formatted version"""
    account_name = account['name']
    account_description = account['description']
    acount_country = account['country']
    return (f"{account_name}, a {account_description} from {acount_country}")





# Display the art
print(logo)

# Generate a random instagram account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

# Format account data into printable format

print(f"Compare A : {print_info(account_a)}")
print(vs)
print(f"Against B: {print_info(account_b)}")
# Ask the user for a guess

guess = input("Who has more followers? Type 'A' or 'B': ")

# Check the user's guess to see whether it's right or wrong.
## Check the follower count of each account
## use if statement to check whether it's right or wrong


# Give the user feedback on whether they are right or wrong:

# Score keeping

# make the game repeatable.

# Make the account at position B to be position A
