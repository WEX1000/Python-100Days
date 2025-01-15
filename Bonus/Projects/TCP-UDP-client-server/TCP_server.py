import socket

HOST = "192.168.1.3"
PORT = 2137

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Tworzenie obiektu serwera
server.bind((HOST, PORT))  # Bindowanie serwera do adresu i portu

server.listen(5)  # Ilość dozwolonych połączeń naraz

while True:
    print(f"Nasłuchiwanie na porcie: {PORT}")
    communication_socket, address = server.accept()  # Przypisywanie portu i adresu użądzenia do zmiennych
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')  # Przypisuje do zmiennej i dekoduje wiadomosc
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got you message! Thank you!".encode('utf-8'))  # Wysyła odpowiedz
    communication_socket.close()  # Zakańcza połączenie
    print(f"Connection with {address} ended!")
