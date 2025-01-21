from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setx(0)
        self.sety(0)
        self.setheading(-315)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() +  self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1