from tkinter import *
root=Tk()

root.title("Harmeet Window's in Python")
root.geometry("200x200")

app=Frame(root)
app.grid()
label=Label(app,text="This is a label:")
label.grid()

btn=Button(app,text="Click Here")
btn.grid()
btn2=Button(app)
btn2.grid()
btn2.configure(text="Press This")
btn3=Button(app)
btn3.grid()
btn3["text"]="Touch Here"

root.mainloop()
