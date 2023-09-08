""" 
 Ignore module 
"""

weight = int(input("Please enter your weight in kgs: "))
height = float(input("Enter your height in metres: "))


bmi = round(weight/(height)**2)

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")
