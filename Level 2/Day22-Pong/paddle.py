from time import sleep
from turtle import Turtle

PADDLE_MOVE = 50

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() > 240:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + PADDLE_MOVE)

    def go_down(self):
        if self.ycor() < -220:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - PADDLE_MOVE)