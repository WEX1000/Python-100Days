from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

test = Turtle()
test.color("white")
test.penup()
test.shapesize(0.0001, 0.0001)
test.goto(0, 280)
test.write("Score", False, align='center', )


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()



screen.exitonclick()