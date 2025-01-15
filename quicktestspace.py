from turtle import Turtle, Screen

rzuf = Turtle()
rzuf.shape("turtle")
rzuf.color("coral")
i = 10

while i < 1000:
    rzuf.speed(1000)
    rzuf.forward(i)
    rzuf.left(150)

    i+=10



my_screen = Screen()
my_screen.exitonclick()