from tkinter import Tk, StringVar, ttk


def pickvalue():
    #print(box.get())
    lbl["text"]=box.get()


root = Tk()

value = StringVar()
box = ttk.Combobox(root, textvariable=value,
                   state='readonly')
box['values'] = ('A', 'B', 'C')
box.current(0)
box.grid(column=2, row=0)

lbl= ttk.Label(text="Welcome")
lbl.grid(column=0, row=2)
btn= ttk.Button(text="Click Here")
btn["command"]=pickvalue
btn.grid(column=3, row=2)



root.mainloop()