from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("coral")

for i in range(1,20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()