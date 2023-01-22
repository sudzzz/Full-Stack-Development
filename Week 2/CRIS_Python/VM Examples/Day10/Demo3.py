#Themed Tkinter Package
from tkinter import ttk
import tkinter

root=tkinter.Tk()

ttk.Style().configure("TButton",padding=20,background="blue")
btn=ttk.Button(text="Click Here")
btn.pack()

root.mainloop()

