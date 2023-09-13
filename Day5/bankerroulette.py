"""
 Write a progrma that selects a random person from a 
 list of names the person will have to pay everyone's bill
"""

import random

# people_list = []

people_input = input("Enter the list of people: ")

people_list = people_input.split(',')

number = len(people_list)

random_number = random.randint(0, number)
random_person = people_list[random_number]
print(f'{random_person} will pay the bill')
