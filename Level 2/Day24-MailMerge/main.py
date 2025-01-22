PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_files:
    letter_content = letter_files.read()
    for name in names:
        new_letter = letter_content.replace(PLACEHOLDER, name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)