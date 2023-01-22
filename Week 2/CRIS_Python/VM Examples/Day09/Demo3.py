from tkinter import *

class Application(Frame):
    def __init__(self,mst):
        Frame.__init__(self,mst)
        self.grid()
        self.create_layout()

    def create_layout(self):
        self.btn1=Button(self,text="Click here")
        self.btn1.grid()

        

root=Tk()
root.title("GUI with Class")
root.geometry("300x300")
app=Application(root)
root.mainloop()