from pymsgbox import password

print("Welcome to Treasure Island. Your mission is to find the treasure.")
i = input("Left or Right")
if i == "Left":
    i = input("Swim or Wait")
    if i == "Wait":
        i = input("With door? Red, Blue, Yellow")
        if i == "Red":
            print("Burned by fire. Game Over")
            pass
        elif i == "Blue":
            print("Eaten by beasts. Game Over.")
            pass
        elif i == "Yellow":
            print("You Win!")
            pass
        else:
            print("Game Over")
            pass
    else:
        print("Attacked by trout. Game Over.")
        pass
else:
    print("Fall into a hole. Game Over.")
    pass

