from tkinter import *

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text="Click Here")
        self.button1.grid()

        self.button2 = Button(self, text="Click Here")
        self.button2.grid()
        self.button2.configure(text="Press")

        self.button3=Button(self)
        self.button3.grid()
        self.button3["text"]="Click"

root=Tk()
root.title("Lazy Buttons")
root.geometry("200x200")

app=Application(root)
root.mainloop()
