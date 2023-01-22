from tkinter import *

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):


        self.button1 = Button(self, text="Click Here")
        self.button1["command"]=self.update_count
        self.button1.grid()


        self.T = Text(self)
        self.T.grid()
    def update_count(self):
        self.button1["text"] = self.T.get('0.0',END)


root=Tk()
root.title("Lazy Buttons")
root.geometry("200x200")

app=Application(root)
root.mainloop()
