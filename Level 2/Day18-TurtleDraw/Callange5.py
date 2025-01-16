from turtle import Turtle, Screen






turtle = Turtle()
turtle.speed("fastest")
turtle.color("coral")

for i in range(72):
    turtle.circle(100)
    turtle.right(5)





screen = Screen()
screen.exitonclick()
screen.setworldcoordinates(-500,-500,500,500)