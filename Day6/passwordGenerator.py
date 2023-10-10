import string
import random

#print(string.ascii_uppercase)
letters = []
numbers = []
characters = list('!@#$%^&*()_')
print(characters)

for letter in string.ascii_lowercase:
    letters.append(letter)

# for letter in string.ascii_uppercase:
#     letters.append(letter)

for number in range(0,11):
    numbers.append(number)


letter_input = input("How many letters would you like in your password? \n")
number_input = input("How many numbers? \n")
character_input = input("How many characters would you like? \n")

password_generated = ''

for char in range(1, int(letter_input)+1):
    char = random.choice(letters)
    password_generated += char

for num in range(1, int(number_input)+1):
    num = random.choice(numbers)
    password_generated += str(num)

for special_char in range(1, int(character_input)+1):
    spec = random.choice(characters)
    password_generated += spec

pw_l = list(password_generated)
random.shuffle(pw_l)

print(''.join(pw_l))
#print(random.shuffle(list(password_generated)))
