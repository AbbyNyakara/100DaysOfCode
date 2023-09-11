"""
 Write code to find the treasure. 
"""

print("Welcome to treasure island. Your goal is to find the treasure.")
direction = input("Do you want to go right or left? ")
if direction.lower() == "left":
    option_1 = input("Do you want to swim or wait? ")
    if option_1.lower() == "wait":
        door = input("What door would you like to go through? \n red, yellow or blue?")
        if door.lower() == "yellow":
            print("You found the treasure. You win!")
        elif door.lower() == "red":
            print("You got burned by fire. Game over!")
        elif door.lower() == "blue":
            print("You got eaten by beasts. You loose!")
        else:
            print("Game over!")
    else:
        print("You were attached by a trout. \n Game over!")
else:
    print("You fell into a hole \n Game Over!")
    