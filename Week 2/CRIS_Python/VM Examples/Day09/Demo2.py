from tkinter import *

root=Tk()
root.title("Python's GUI Programming")
root.geometry("200x300")

app=Frame(root)
app.grid()

lbl=Label(app,text="This Is Label")
lbl.grid()

btn1=Button(app,text="Click Here")
btn1.grid()

btn2=Button(app)
btn2.configure(text="Press This Button")
btn2.grid()

btn3=Button(app)
btn3["text"]="Press Me"
btn3.grid()

root.mainloop()