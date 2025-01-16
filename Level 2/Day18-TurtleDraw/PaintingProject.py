import random
from turtle import Turtle, Screen

color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

turtle = Turtle()
#turtle.speed("fastest")
turtle.color("coral")
turtle.penup()

turtle.teleport(-400, 400)

for i in range(10):
    for j in range(10):
        turtle.dot(20, random.choice(color))
        turtle.forward(70)
    if i % 2 == 1:
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
    else:
        turtle.right(90)
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(70)









screen = Screen()
screen.exitonclick()
screen.setworldcoordinates(-500,-500,500,500)