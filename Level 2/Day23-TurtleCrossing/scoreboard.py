from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write_()

    def write_(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_point(self):
        self.level += 1
        self.clear()
        self.write_()

    def game_over(self):
        self.goto(-100, -20)
        self.write("Game Over!", align="left", font=FONT)