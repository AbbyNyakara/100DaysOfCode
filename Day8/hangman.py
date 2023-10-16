"""
 Refer to the attached image
"""
import random
# Generate random words

words = ["baboon", "camel", "amiss", "cold", "challenge"]
random_word = random.choice(words)

print(random_word)

#create as many blanks as the letters in the word
quiz = []
for letter in random_word:
    quiz += "_"

print(quiz)
# Ask the user to guess a letter
guess = input("Guess a letter: \n")

# Check if the letter is in the word
if guess in random_word:
    #Replace the letter in the blank
    print("a")
else:
    print("no")
