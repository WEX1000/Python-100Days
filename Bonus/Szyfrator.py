import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import random
import string


# Funkcja do generowania losowego klucza
def generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))


# Funkcja szyfrująca plik
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Padding danych do wielokrotności bloku 16
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Inicjalizacja AES w trybie CBC
    iv = os.urandom(16)  # Losowy wektor inicjalizacyjny
    cipher = Cipher(algorithms.AES(key.encode()), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Zapisanie zaszyfrowanych danych do nowego pliku
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as enc_file:
        enc_file.write(iv + encrypted_data)

    # Usuwanie oryginalnego pliku
    os.remove(file_path)

    return encrypted_file_path


# Funkcja do szyfrowania zawartości folderu
def encrypt_folder(folder_path):
    key = generate_key()
    print(f'Generated key: {key}')

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)


# Hardcodowana ścieżka folderu
folder_path = 'D:/TEST'  # Zmień na odpowiednią ścieżkę
encrypt_folder(folder_path)
