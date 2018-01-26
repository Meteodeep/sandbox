#Edit function to change shape
import random
from turtle import *
canvas = Screen()

number = random.randrange(0, 800)


turtle = Turtle()

for i in range(4):
    turtle.forward(100) #number
    turtle.left(90)  #number

canvas.exitonclick()

