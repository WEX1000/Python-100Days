import random

words = [
    "apple", "banana", "orange", "grape", "cherry",
    "table", "chair", "window", "mirror", "carpet",
    "school", "teacher", "student", "pencil", "notebook",
    "garden", "flower", "tree", "cloud", "mountain"
]
GameWord = list(words[random.randint(0, 19)])

print(GameWord)
for i in range(1,10):
    print('\n')



