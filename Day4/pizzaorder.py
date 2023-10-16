"""
small_pizza: $15
medium pizza: $20
large pizza: $25

pepperoni for small pizza: $2
pepperoni for medium and Large pizza: $3

extra cheese for any pizza: $1

"""

print("Please order your pizza")
bill = 0

size = input("What size of pizza would you like? S, M or L: ").upper()
pepperoni = input("Would you like pepperoni? Y or N: ").upper()
cheese = input("Would you like cheese? Y or N: ").upper()

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1

print(f"Your total bill is {bill}")
