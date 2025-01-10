import random

#   Real cards symulation

Game = True



def randomnumber():
    return random.randint(2, 10)

def finalraport(pcards, dcards):
    print('Your cards: ', end='')
    for i in range(len(pcards)):
        print(f'[{pcards[i]}]', end='')
    print(f', your sum is {sum(pcards)}')
    print('Dealer cards: ', end='')
    for i in range(len(dcards)):
        print(f'[{dcards[i]}]', end='')
    print(f', dealer sum is {sum(dcards)}')

def endgame(pcards, dcards):
    if sum(dcards) > 21:
        print('\nYou won')
        finalraport(pcards, dcards)
    elif sum(pcards) > 21:
        print('\nYou loose')
        finalraport(pcards, dcards)
    else:
        if sum(dcards) > sum(pcards):
            print('\nYou loose')
            finalraport(pcards, dcards)
        elif sum(dcards) < sum(pcards):
            print('\nYou win')
            finalraport(pcards, dcards)
        else:
            print('\nDraw')
            finalraport(pcards, dcards)

while Game:

    pcards = []
    dcards = []

    gameloop = input("Do you want to plan? y/n ")
    if gameloop == "n":
        Game = False
        break

    pcards.append(randomnumber())
    pcards.append(randomnumber())
    dfirstcard = randomnumber()
    dcards.append(dfirstcard)

    while sum(dcards) < 17:
        dcards.append(randomnumber())


    print(f'Your cards: [{pcards[0]},{pcards[1]}] current score: {int(pcards[0])+int(pcards[1])}')
    print(f'Dealers first card: {dfirstcard}')
    sh = input("Stand or hit? s/h ")
    if sh == "h":
        while True:
            pcards.append(randomnumber())
            if sum(pcards) > 21:
                break
            print("Your cards", end="")
            for i in range(len(pcards)):
                print(f'[{pcards[i]}]', end='')
            print(f", your sum is {sum(pcards)}")
            sh = input("Stand or hit? s/h ")
            if sh != "h":
                break
    endgame(pcards, dcards)
    for i in range(1, 4): print("")