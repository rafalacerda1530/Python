from tkinter import *

root = Tk()
root.title('OLA')
var = StringVar()
label = Label(root, font=("Arial", 12), bg="red", fg="green", textvariable=var, relief=RAISED)

var.set(f"Hey!? How are you doing {nome}?")
label.pack()
root.mainloop()