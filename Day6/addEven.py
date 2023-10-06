"""
 Create a program that takes the user input of a number. It will then sum up all the
 even numbers between 0 and the input
"""

input_num = int(input("Enter a number between 0 and 1000: \n"))

sum_nums = 0

for num in range(0, input_num+1, 2):
    sum_nums += num

print(f"The sum of all even numbers between 0 and {input_num} is {sum_nums}")
