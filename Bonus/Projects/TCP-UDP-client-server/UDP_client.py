import socket

HOST = "51.83.132.29"
PORT = 2142

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Tworzenie obiektu, rodzaj połączenia, TCP lub UDP

client.sendto("Hello dziadu!".encode(), (HOST, PORT))
data, addres = client.recvfrom(1024)
print(data.decode())
