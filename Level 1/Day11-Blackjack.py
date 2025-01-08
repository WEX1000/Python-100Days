import random

#   Real cards symulation

Game = True
pcards = []
dcards = []
dcardssum = 0
dfirstcard = 0


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


while Game:
    gameloop = input("Do you want to plan? y/n ")
    if gameloop == "n":
        Game = False
        break

    pcards.append(randomnumber())
    pcards.append(randomnumber())
    dfirstcard = randomnumber()
    dcards.append(dfirstcard)
    dcardssum += dfirstcard

    while dcardssum < 17:
        a = randomnumber()
        dcards.append(a)
        dcardssum += a

    print(f'Your cards: [{pcards[0]},{pcards[1]}] current score: {int(pcards[0])+int(pcards[1])}')
    print(f'Dealers first card: {dfirstcard}')
    sh = input("Stand or hit? s/h ")
    if sh == "s":
        if dcardssum > 21:
            print('\nYou won')
            finalraport(pcards, dcards)
        else:
            if dcardssum > sum(pcards):
                print('\nYou loose')
                finalraport(pcards, dcards)
            elif dcardssum < sum(pcards):
                print('\nYou win')
                finalraport(pcards, dcards)
            else:
                print('\nDraw')
                finalraport(pcards, dcards)
    elif sh == "h":
        pass
    else:
        print('Bad choice')
        break





