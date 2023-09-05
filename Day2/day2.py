# Indexing - start at 0
print("Hello"[0]) # Prints H

# Printing the last character 
print("Hello"[-1])

# The undescore makes the code readable as if we had commas instead
print(1_000_000)

# Write a program that adds the digits in a number: 
# Example: if the input was 35, the output should be 3 + 5 = 8 

# number = input(" Enter a two-digit number: \n")

# str_number = str(number)
# num_1 = int(str_number[0])
# num_2 = int(str_number[1])

# result = num_1 + num_2
# print(f"The result is {result}") 

# Create a BMI Calculator
height = input("What is your height: ")
weight = input("What is your weight in kgs? ")

height = float(height)  # This cannot be int. Check the error we get
weight= int(weight)

bmi = weight/(height ** 2)
print(f"Your BMI is {bmi}")