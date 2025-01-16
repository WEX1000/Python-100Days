import turtle as t
import random



tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
j = 0
pos = []


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


while j < 1000:
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
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
    print(f'Status: {j}/1000')
    pos.append(tim.pos()[1])
    tim.teleport(0, 0)

round_pos = [round(num, 4) for num in pos]
round_pos.sort()
print(round_pos)
print(f'Max: {max(round_pos)}')
print(f'Min: {min(round_pos)}')
print(f'Suma: {sum(round_pos)}')

with open("Wyniki.txt", 'a')as file:
    file.write(f"Test 1\n")
    file.write(f"Rounds: {j}\n")
    file.write(f'Max: {max(round_pos)}\n')
    file.write(f'Min: {min(round_pos)}\n')
    file.write(f'Suma: {sum(round_pos)}\n')
    file.write("\n")


screen = t.Screen()
screen.exitonclick()


