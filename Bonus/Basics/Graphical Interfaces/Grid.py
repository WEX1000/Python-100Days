import tkinter as tk

root = tk.Tk() # Okno podstawowe

root.geometry("500x500") # Wymiary okna
root.title("My first GUI") # Nazwa okna

label = tk.Label(root, text="Hello World", font=('Arial', 18)) # Etykieta
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16)) # Textbox
textbox.pack(padx=10)

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

btn1 = tk.Button(frame, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(frame, text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(frame, text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(frame, text='4', font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(frame, text='5', font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(frame, text='6', font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

frame.pack(fill='x')

root.mainloop() # Główna pętla

