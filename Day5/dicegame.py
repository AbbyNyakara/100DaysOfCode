"""
 random  module
"""
import random

# Create a random coin toss program. 1- heads, 0-tails.
random_number = random.randint(0,1)

if random_number == 0:
    print("Tails")
else:
    print("Heads")