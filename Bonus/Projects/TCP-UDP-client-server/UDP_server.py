import socket

HOST = "192.168.1.3"
PORT = 2137

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Tworzenie obiektu serwera
server.bind((HOST, PORT))  # Bindowanie serwera do adresu i portu

while True:
    data, addres = server.recvfrom(1024)
    print(data.decode())
    server.sendto('Hello from server'.encode(), addres)