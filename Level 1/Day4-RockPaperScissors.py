import random


def returnasci(choice):
    if choice == 0:
        return """
                    _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)
                """
    elif choice == 1:
        return """
                     _______
                ---'    ____)____
                           ______)
                          _______)
                         _______)
                ---.__________)
                """
    else:
        return """
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
                """

user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors"))
computer_choice = random.randint(0,2)
print(f'Your choice: {returnasci(user_choice)}')
print(f'Computer choice: {returnasci(computer_choice)}')
if user_choice == 0:  # User rock
    if computer_choice == 0:
        print("Draw!")
        pass
    elif computer_choice == 1:
        print("You loose!")
        pass
    else:
        print("You win!")
        pass
elif user_choice == 1:  # User paper
    if computer_choice == 0:
        print("You win!")
        pass
    elif computer_choice == 1:
        print("Draw!")
        pass
    else:
        print("You loose!")
        pass
elif user_choice == 2:  # User scissors
    if computer_choice == 0:
        print("You loose!")
        pass
    elif computer_choice == 1:
        print("You win!")
        pass
    else:
        print("Draw!")
        pass
else:
    print("Wrong choice")
    pass