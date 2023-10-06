import random

game_choices = ['Rock', 'Paper', 'Scissors']
choice = input('What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors: ')
your_choice = game_choices[int(choice)]
print(f'You chose {your_choice}')

random_computer_choice = random.randint(0, 2)
computer_choice = game_choices[random_computer_choice]
print(f" The computer chose {computer_choice}")

if your_choice == 'Rock' and computer_choice == "Scissors":
    print("You won")
elif your_choice == 'Scissors' and computer_choice == "Paper":
    print("You win")
elif your_choice == 'Paper' and computer_choice == "Rock":
    print('You win')
elif computer_choice == 'Rock' and your_choice == "Scissors":
    print('The computer won')
elif computer_choice == 'Scissors' and your_choice == "Paper":
    print("The computer won")
elif computer_choice == 'Paper' and your_choice == "Rock":
    print('The computer won')
else:
    print("It's a tie")


