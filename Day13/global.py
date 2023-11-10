# This is however not the best way of dealing with global scope. 
# This is prone to errors
# Problematic code
enemies = 1 

def increase_enemies():
    global enemies
    enemies += 1
    print(f"The total numner of enemies is {enemies}")

increase_enemies()


# Here is a better way: 

friends = 1

def increase_friends():
    return friends + 1

print(increase_friends())
