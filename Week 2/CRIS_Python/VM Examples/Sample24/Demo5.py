from tkinter import ttk
import tkinter

root=tkinter.Tk()

ttk.Style().configure("TButton",padding=20,relief="flat",background="blue")
btn=ttk.Button(text="Sample")
btn.pack()
root.mainloop()