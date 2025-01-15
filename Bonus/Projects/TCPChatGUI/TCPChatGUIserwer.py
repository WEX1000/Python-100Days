import threading
import socket

HOST = "127.0.0.1"
PORT = int(input("Podaj port:"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []
addresses = []


def brodecast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            brodecast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                print(f'{nickname} left the chat')
                nicknames.remove(nickname)
            break


def recive():
    while True:
        client, address = server.accept()
        #print(f'Connected with {str(address)}')
        #client.send('NICK'.encode('ascii'))

        nickname = client.recv(1024).decode('ascii')

        nicknames.append(nickname)
        clients.append(client)
        addresses.append(address)
        #print(f'Nickname of the clinet is {nickname}')
        client.send('Connected to the server\n'.encode('ascii'))

        print('----------')
        for i in range(len(clients)):
            print(f' Nickname: {nicknames[i]} | Addres: {addresses[i]} | Client: {clients[i]} |')
        print('----------')

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == '__main__':
    print("Server is listening")
    recive()
