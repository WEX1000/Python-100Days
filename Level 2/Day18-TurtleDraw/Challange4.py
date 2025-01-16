from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]
color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

print(random.choice(direction))

turtle = Turtle()
turtle.pensize(10)
turtle.speed("fastest")


for i in range(1,100):
    turtle.color(random.choice(color))
    turtle.right(random.choice(direction))
    turtle.forward(10)


screen = Screen()
screen.exitonclick()