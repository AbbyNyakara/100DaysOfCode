from random import randint

# Declare the number of turns for each constant for each level.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess vs the answer

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The answe is {answer}")

# Create a function to choose a difficulty:
# It will take the user's input and assign the number of tries they have: 

def choose_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def game():
    answer = randint(1,100)
    print(f"Psst the answer is {answer}")
    print("Welcome to the number guessing game: ")
    print("I am thinking of a number between 1 and 100")

    # Ask the user to choose the difficulty:
    turns = choose_difficulty()

    print(f"You have {turns} tries to guess the number: ")

    guess = 0
    while guess != answer:
        guess = int(input("Guess the number: "))

        # Call the check answer function to check the answer: 

        # Reassign the value of turns to be the output from the fucntion: 
        turns = check_answer(guess, answer, turns)
        print(f"You have {turns} chances remaining.")
        if turns == 0:
            print("You've run out of guesses. You lose")
            return

game()