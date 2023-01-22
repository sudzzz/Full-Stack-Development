from tkinter import *

class Application(Frame):
    def __init__(self, mst):
        Frame.__init__(self, mst)
        self.grid()
        self.create_layout()

    def create_layout(self):
        self.btn1 = Button(self)
        self.btn1["text"] = "Counter : "
        self.btn1["command"] = self.update_count
        self.btn1.grid()

        self.T=Text(self)
        self.T.configure(width=20)
        self.T.configure(height=2)
        self.T.grid()

        self.lbl=Label(self,text="Initial Value")
        self.lbl.grid()

    def update_count(self):
        self.lbl["text"] = self.T.get('0.0',END)


root = Tk()
root.title("GUI with Class")
root.geometry("300x300")
app = Application(root)
root.mainloop()