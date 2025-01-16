from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="With turtle will win the race? Enter a color: ")
colors = ["red", "orange",  "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-120 + (i * 50))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print("You won!")
            else:
                print("You loose!")
            is_race_on = False
            break

        turtle.forward(random.randint(0, 10))


screen.listen()
screen.exitonclick()





