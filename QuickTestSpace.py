import turtle as t
import random



tim = t.Turtle()
j = 0
pos = []

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.speed("fastest")
tim.color("red")
tim.forward(707.11)
tim.teleport(0, 100)
tim.forward(707.11)
tim.teleport(0, 200)
tim.forward(707.11)
tim.teleport(0, -100)
tim.forward(707.11)
tim.teleport(0, -200)
tim.forward(707.11)
tim.left(90)
tim.forward(400)
tim.teleport(0, -200)
tim.forward(400)
tim.right(90)
tim.teleport(0, 0)


while j < 2:
    tim.color(colours[j])
    i = 0
    while i < 100:
        if random.randint(1,100) % 2 == 0:
            tim.right(45)
            tim.forward(10)
            tim.left(45)
        else:
            tim.left(45)
            tim.forward(10)
            tim.right(45)
        i += 1
    j += 1
    pos.append(tim.pos())
    tim.teleport(0, 0)

print(pos)

tim.right(45)
tim.forward(1000)
a = tim.pos()
print(a[1])
print(tim.pos())

screen = t.Screen()
screen.exitonclick()


