import random

words = [
    "apple", "banana", "orange", "grape", "cherry",
    "table", "chair", "window", "mirror", "carpet",
    "school", "teacher", "student", "pencil", "notebook",
    "garden", "flower", "tree", "cloud", "mountain"
]
GameWord = list(words[random.randint(0, 19)])

for i in range(len(GameWord)):
    input(f"What your letter? No.{i}")



