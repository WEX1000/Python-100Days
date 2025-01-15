import socket

HOST = "51.83.132.29"
PORT = 2142

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Tworzenie obiektu, rodzaj połączenia, TCP lub UDP
socket.connect((HOST, PORT))  # Łączenie do podanego adresu

socket.send("Hello dziadu!".encode('UTF-8'))
print(socket.recv(1024).decode('UTF-8'))
