# Import the data
import random
from art import logo, vs
from data import data

# Create the logo
print(logo)

# Randomly select the items to be compared:

def choose_player():
    """Generates a item from the data list"""
    return(random.choice(data))













# Assign the first to A
# Assign the second to B 
a = choose_player()
b = choose_player()

if a == b:
    b = choose_player()

print(a)
print(b)

# Print out the parties to compare

print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
print(vs)
print(f"Against B: {b['name']}, a {b['description']} from {b['country']}")

player_guess = input("Who has more players. Type 'A' or 'B': ").lower()

# Comapre their instagram followers: 

followers_a = a['follower_count']
followers_b = b['follower_count']

# Find the follower with the highest 
highest = max(followers_a, followers_b)
print(highest)

# Define the winner 

score = 0


# Check if the user is right:

if player_guess






# If correct, increase the score by 1
# Assign the item in B to A and generate a new one for A
# If wrong, exit the game, and print out the score. 