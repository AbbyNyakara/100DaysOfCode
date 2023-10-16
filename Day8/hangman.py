import random
import words
import art

print(art.logo)
words = words.word_list
random_word = random.choice(words)

word_length = len(random_word)

blank_list = []
for _ in range(word_length):
    blank_list += "_"

print(blank_list)

end_of_game = False
lives = 6

while not end_of_game:
    user_guess = input("Guess a letter \n").lower()

    for position in range(word_length):
        if user_guess == list(random_word)[position]:
            blank_list[position] = user_guess

    if user_guess not in random_word:
        lives -= 1
        print(art.stages[lives])
        if lives == 0:
            print("You loose!")
            end_of_game = True
           
    print(blank_list)

    if "_" not in blank_list:
        end_of_game = True
        print("You win!")

