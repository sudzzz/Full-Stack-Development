from tkinter import *
class Application(Frame):
    def __init__(self,mst):
        Frame.__init__(self,mst)
        self.grid()
        self.lbl1 = Label(self, text="No. of Records : " + str(round(len(open("employee.txt", "r").readlines())/6,0)))
        self.lbl1.grid()
        self.lst=["Enter Code","Enter Name","Enter Salary","Enter Jan Month Salary","Enter Feb Month Salary"]
        self.lstc=[]
        self.create_layout()
    def create_layout(self):
        for l in self.lst:
            self.lbl1 = Label(self, text=l)
            self.lbl1.grid()
            self.T1 = Text(self)
            self.T1.configure(width=20, height=2)
            self.T1.grid()
            self.lstc.append(self.T1)

        self.btn1 = Button(self)
        self.btn1["text"] = "SUBMIT"
        self.btn1["command"] = self.update_count  # property other than text to perform a paricular task
        self.btn1.grid()
    def update_count(self):
        st=""
        for f in self.lstc:
            st+=(f.get('0.0',END))

        open("employee.txt", "a").write(st + ':')

root=Tk()
root.title("GUI with class")
root.geometry("200x400")
app=Application(root)
root.mainloop()