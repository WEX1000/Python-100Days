import tkinter as tk

root = tk.Tk() # Okno podstawowe

root.geometry("500x500") # Wymiary okna
root.title("My first GUI") # Nazwa okna

label = tk.Label(root, text="Hello World", font=('Arial', 18)) # Etykieta
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16)) # Textbox
textbox.pack(padx=10)

myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

button = tk.Button(root, text="Click me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop() # Główna pętla

