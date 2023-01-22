from tkinter import Tk,ttk

def pickvalue():
    lbl["text"]=box.get()

root = Tk()

box = ttk.Combobox(root,state='readonly')
box['values'] = ('India', 'Australia', 'Pakistan')
box.current(0)
box.grid(column=2, row=0)

lbl= ttk.Label(text="Countries")
lbl.grid(column=0, row=2)
btn= ttk.Button(text="Click Here")
btn["command"]=pickvalue
btn.grid(column=3, row=2)



root.mainloop()