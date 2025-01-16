from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("coral")
turtle.speed(1000)

for i in range(3,110):
    for j in range(i):
        turtle.forward(100)
        turtle.right(360/i)


screen = Screen()
screen.exitonclick()