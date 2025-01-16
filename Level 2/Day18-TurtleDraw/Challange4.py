from turtle import Turtle, Screen
import random

direction = [0, 90, 180, -90]
color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

print(random.choice(direction))

turtle = Turtle()
turtle.pensize(5)
#turtle.speed("fastest")


for i in range(1,1000):
    turtle.color(random.choice(color))
    turtle.right(random.choice(direction))
    turtle.forward(50)


screen = Screen()
screen.exitonclick()
screen.setworldcoordinates(-500,-500,500,500)