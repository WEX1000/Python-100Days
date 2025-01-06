import random

words = [
    "apple", "banana", "orange", "grape", "cherry",
    "table", "chair", "window", "mirror", "carpet",
    "school", "teacher", "student", "pencil", "notebook",
    "garden", "flower", "tree", "cloud", "mountain"
]
stages = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
GameWord = random.choice(words)
display =  ""
placeholder = ""
game_over = False
correct_letters = []
lives = 0

for position in range(len(GameWord)):
    placeholder += "_"
print(placeholder)

while not game_over:
    print(stages[lives])
    display = ""

    guess = input("\nGuess a letter: ").lower()
    if guess not in GameWord:
        print("Bad letter!")
        lives += 1

    if lives == 6:
        game_over = True
        print("You loose!")
        print(stages[6])
        break

    for letter in GameWord:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")

