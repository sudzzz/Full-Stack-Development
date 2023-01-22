from tkinter import *

class Application(Frame):
    def __init__(self, mst):
        Frame.__init__(self, mst)
        self.grid()
        self.counter=0
        self.create_layout()

    def create_layout(self):
        self.btn1 = Button(self)
        self.btn1["text"]="Counter : "
        self.btn1["command"] = self.update_count
        self.btn1.grid()

    def update_count(self):
        self.counter +=1
        self.btn1["text"] = "Counter : "  + str(self.counter)

root = Tk()
root.title("GUI with Class")
root.geometry("300x300")
app = Application(root)
root.mainloop()