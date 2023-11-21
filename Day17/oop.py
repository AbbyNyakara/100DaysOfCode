#attributes - what they have 
# methods - similar to functions 
TK_SILENCE_DEPRECATION=1

#import the Turtle class from the turtle module: 
from turtle import Turtle, Screen

# Create a turtle object: 
turtle = Turtle()
turtle.shape("turtle")

turtle.color("coral")


screen = Screen()
print(screen.canvheight)
screen.exitonclick()
