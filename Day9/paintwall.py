# Write a program that calcukates how many cans you need to buy to paint a wall
# 1 can of paint can paint 5 sq.metres

import math

def paint_wall(height, width, coverage):
    number_of_cans = math.ceil((height*width)/coverage)
    print(f" You need {number_of_cans} cans of paint")

paint_wall(5,7, 2)