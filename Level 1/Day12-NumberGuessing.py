import random

from scrapy.utils.trackref import live_refs

number = random.randint(0, 100)
choose = input("Choose: Easy(e), Hard(h)")
if choose == "h":
    lives = 5
else:
    lives = 10
while True:
    print(f'Lives: {lives}')
    guess = int(input("Podaj numer: "))
    if guess > number:
        print("Less")
    elif guess < number:
        print("More")
    else:
        print(f"Thats right the number is {number}")
        break
    lives -= 1
    if lives == 0:
        print("You loose")
        break