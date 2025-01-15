import tkinter as tk
import socket
import threading

nickname = ""
password = ""
HOST = ""
PORT = 0
stop_thread = False
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#----------------------------------------Import, Variable, Server Start------------------------------#
#----------------------------------------------------------------------------------------------------#
#----------------------------------------Main GUI----------------------------------------------------#

class MyGUI:

    def __init__(self):

        self.message = None
        self.root = tk.Tk()

        self.root.geometry("800x550")
        self.root.title("TCP chat 0.4")

        self.frame= tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

        self.label = tk.Label(self.root, text=f'Logged as: {nickname}', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=10, font=('Arial', 18), state='disabled')
        self.textbox.pack(padx=10, pady=10)

        self.sendbox = tk.Text(self.root, height=1, font=('Arial', 18))
        self.sendbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.frame, text="Send Message", font=('Arial', 18), command=self.send_message)
        self.button.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.buttonConnect = tk.Button(self.frame, text="Connect", font=('Arial', 18), command=self.connect_to_chat)
        self.buttonConnect.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.buttonKill = tk.Button(self.frame, text="Zakończ", font=('Arial', 18), command=self.kill_thread)
        self.buttonKill.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()
        
        self.frame.pack(fill='x')
        self.root.mainloop()

    def display_message(self, message):
        self.textbox.config(state='normal')
        self.textbox.insert(tk.END, message)
        self.textbox.config(state='disabled')
        self.textbox.see(tk.END)

    def send_message(self):
        client.send(str(f'{nickname}: ' + self.sendbox.get('1.0', tk.END)).encode('ascii'))
        self.sendbox.delete('1.0', tk.END)

    def connect_to_chat(self):
        global client, HOST, PORT
        client.send(nickname.encode('ascii'))

    def kill_thread(self):
        global stop_thread, client
        stop_thread = True
        try:
            client.shutdown(socket.SHUT_RDWR)
            client.close()
        except:
            pass
        self.root.destroy()

    def receive(self):
        while True:
            if stop_thread:
                break
            try:
                self.message = client.recv(1024).decode('ascii')
                self.display_message(self.message)
            except:
                client.close()
                break


#----------------------------------------Main GUI----------------------------------------------------#
#----------------------------------------------------------------------------------------------------#
#----------------------------------------Login Panel-------------------------------------------------#

def send_data():
    global nickname, password, HOST, PORT
    nickname = myentryLogin.get()
    password = myentryPass.get()
    HOST = myentryIP.get()
    PORT = myentryPort.get()
    login.destroy()

login = tk.Tk()
login.geometry("400x200")
login.title("Zaloguj się!")

frame = tk.Frame(login)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

labelLogin = tk.Label(frame, text="Login", font=('Arial', 18)) # Etykieta
labelLogin.grid(row=0, column=0, sticky=tk.W+tk.E)

myentryLogin = tk.Entry(frame)
myentryLogin.grid(row=1, column=0, sticky=tk.W+tk.E)

labelPass = tk.Label(frame, text="Password", font=('Arial', 18)) # Etykieta
labelPass.grid(row=2, column=0, sticky=tk.W+tk.E)

myentryPass = tk.Entry(frame)
myentryPass.grid(row=3, column=0, sticky=tk.W+tk.E)

labelIP = tk.Label(frame, text="IP", font=('Arial', 18)) # Etykieta
labelIP.grid(row=0, column=1, sticky=tk.W+tk.E)

myentryIP = tk.Entry(frame)
myentryIP.grid(row=1, column=1, sticky=tk.W+tk.E)

labelPort = tk.Label(frame, text="PORT", font=('Arial', 18)) # Etykieta
labelPort.grid(row=2, column=1, sticky=tk.W+tk.E)

myentryPort = tk.Entry(frame)
myentryPort.grid(row=3, column=1, sticky=tk.W+tk.E)

buttonSend = tk.Button(login, text="Confirm", font=('Arial', 18), command=send_data)
buttonSend.pack(padx=10, pady=10)

frame.pack(fill='x')
login.mainloop()

#----------------------------------------Login Panel-------------------------------------------------#
#----------------------------------------------------------------------------------------------------#
client.connect((HOST, int(PORT)))
MyGUI()
