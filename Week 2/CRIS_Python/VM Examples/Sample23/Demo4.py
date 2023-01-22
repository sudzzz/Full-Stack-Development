from tkinter import *

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks=0
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text="Click Here")
        self.button1["text"]="Total"
        self.button1["command"]=self.update_count
        self.button1.grid()

    def update_count(self):
        self.button_clicks +=1
        self.button1["text"]="Total " +str(self.button_clicks)
root=Tk()
root.title("Lazy Buttons")
root.geometry("200x200")

app=Application(root)
root.mainloop()
