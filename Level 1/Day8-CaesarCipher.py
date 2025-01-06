letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted = ""
    worklist = list(text)
    for letter in worklist:
        if letter == " ":
            encrypted += " "
        else:
            i = letters.index(letter)
            if i + shift < 26:
                encrypted += letters[i+shift]
            else:
                encrypted += letters[i+shift-26]
    print(encrypted)

def decrypt(text, shift):
    decrypted = ""
    worklist = list(text)
    for letter in worklist:
        if letter == " ":
            decrypted += " "
        else:
            i = letters.index(letter)
            if i - shift >= 0:
                decrypted += letters[i - shift]
            else:
                decrypted += letters[i - shift + 26]
    print(decrypted)


direction = input("Type 'encode' or 'decode\n")
text = input("Type the message:\n")
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Wrong option")