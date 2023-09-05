# Write a program that calculates how many weeks you have left if you were to live to 90 years old
# Should output the days, weeks and months 


age = input('What is your age? ')
 
time_left = 90 - int(age)

days = time_left * 365
months = time_left * 12
weeks = time_left * 52

print(f"You have {days} days, {weeks} weeks and {months} months remaining")

