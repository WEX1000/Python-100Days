import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Funkcja odszyfrowująca plik
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Oddzielenie wektora inicjalizacyjnego (IV) od zaszyfrowanych danych
    iv = data[:16]
    encrypted_data = data[16:]

    # Inicjalizacja AES w trybie CBC
    cipher = Cipher(algorithms.AES(key.encode()), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Usunięcie paddingu
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Zapisanie odszyfrowanych danych do nowego pliku
    decrypted_file_path = file_path[:-4]  # Usunięcie rozszerzenia '.enc'
    with open(decrypted_file_path, 'wb') as dec_file:
        dec_file.write(unpadded_data)

    # Usuwanie zaszyfrowanego pliku
    os.remove(file_path)

    return decrypted_file_path

# Funkcja do odszyfrowania zawartości folderu
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.enc'):  # Tylko pliki zaszyfrowane
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)

# Podanie klucza i ścieżki folderu
key = input("Enter decryption key: ")
folder_path = 'D:/TEST'  # Zmień na odpowiednią ścieżkę
decrypt_folder(folder_path, key)
