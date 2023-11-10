import random

# Define the random number:
number = random.randint(1, 100)

print(f"psssst! the number is {number}")

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

# Define the number of attemps for the easy and hard levels: 10 for easy and 5 for hard:
attempts  = 0
game_on = True
# Create the attempt guess function
def guess():
    global attempts 
    global game_on
    
    make_guess = int(input("Guess the number: "))
    if make_guess < number:
        attempts  -= 1
        return "Too low. Guess Again"
    
    elif make_guess > number:
        attempts  -= 1
        return "Too high. Guess Again"
    else:
        game_on = True
        return f"Thats right. The number is {make_guess}"
        

if difficulty_level == 'hard':
    attempts  = 5
    while game_on: 
        print(f"You have {attempts} attempts  to guess the number")
        guess()
        if attempts == 0:
            game_on = False
else:
    attempts  = 10
    print(f"You have {attempts } attempts to guess the number")
    guess()








