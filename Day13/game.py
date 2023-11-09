import random

# Constants:

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

# Functions:
def choose_difficulty(level):
    """Takes the chosen level of difficulty and prints out the remaining attempts"""
    if level == 'easy':
        turns = EASY_LEVEL_TURNS
        print(f"You have {turns} attempts remaining to guess the number")
    else:
        turns = HARD_LEVEL_TURNS
        print(f"You have {turns} attempts remaining to guess the number")


def play_game(guess, answer):
    if guess > answer:
        print("Too high. Guess Again")
        turns -= 1
    elif guess < answer:
        print("Too low. Guess Again")
        turns -= 1
    else:
        print(f"You got it right. The answer is {answer}")





# The game: 
print("Welcome to the number guessing game: ")
print("I am thinking of a number between 1 and 100")

answer = random.randint(1, 100)
print(f"Psst the answer is {answer}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
choose_difficulty(level)

guess = int(input("Make a guess: "))
play_game(guess, answer)

