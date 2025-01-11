import random

from urllib3.filepost import choose_boundary

data = [
    {"name": "New York", "population": 8410000},
    {"name": "Los Angeles", "population": 3980000},
    {"name": "Tokyo", "population": 14000000},
    {"name": "London", "population": 9300000}
]
Game = True
startvalue = random.randint(0,3)
score = 0

while Game:
    print()
    print(f"Score: {score}")
    print()
    print(f'City {data[startvalue]['name']} have population of {data[startvalue]['population']} ')
    gamevalue = random.randint(0,3)
    if gamevalue == startvalue:
        gamevalue += 1
    choose = int(input(f'Do you think {data[gamevalue]['name']} have more or less population? 1 for more, 2 for less'))
    print(f"choice: {choose}")
    if choose == 1:
        if int(data[gamevalue]['population']) > int(data[startvalue]['population']):
            print("You won")
            startvalue = gamevalue
            score += 1
        else:
            print("You loose, start over")
            startvalue = random.randint(0, 3)
            break
    if choose == 2:
        if int(data[gamevalue]['population']) < int(data[startvalue]['population']):
            print("You won")
            startvalue = gamevalue
            score += 1
        else:
            print("You loose, start over")
            startvalue = random.randint(0, 3)
            break