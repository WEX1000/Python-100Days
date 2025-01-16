from turtle import Turtle, Screen

turtle = Turtle()

screen = Screen()


def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.back(10)

def turn_left():
    new_heading = turtle.heading() + 45
    turtle.setheading(new_heading)

def turn_right():
    new_heading = turtle.heading() - 45
    turtle.setheading(new_heading)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()





