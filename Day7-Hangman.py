import random

words = [
    "apple", "banana", "orange", "grape", "cherry",
    "table", "chair", "window", "mirror", "carpet",
    "school", "teacher", "student", "pencil", "notebook",
    "garden", "flower", "tree", "cloud", "mountain"
]
GameWord = list(words[random.randint(0, 19)])
lives = 5
while lives > 0:
    print(GameWord)
    letter = input()
    for i in range(len(GameWord)):
        print(GameWord[i] == letter)