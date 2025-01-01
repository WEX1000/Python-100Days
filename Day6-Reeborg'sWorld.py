# reeborg.ca
# Humble 4
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()
'''
# Maze
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear() and front_is_clear():
        turn_right()
        move()
    elif not right_is_clear() and front_is_clear():
        move()
    elif right_is_clear() and not front_is_clear():
        turn_right()
        move()
    elif not right_is_clear() and not front_is_clear():
        turn_left()
    else:
        move()
'''