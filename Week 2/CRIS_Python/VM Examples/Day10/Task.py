#how to open different window from main window
import tkinter as tk

class MainWindow(tk.Frame):
    counter=0
    Lst=["Add Employee","Mark Attendance","Show Attendance","Exit"]

    def Navigate(self, ar=4):
        print(ar)
    def __init__(self,mst):
        tk.Frame.__init__(self,mst)
        for ls in self.Lst:
            #self.bt1=tk.Button(self,text=ls,command=self.Navigate(ls))
            self.bt1 = tk.Button(self, text=ls)
            self.bt1.bind('<bt1>')
            self.bt1.pack()


    def create_win(self):
        #print("clicked")
        self.counter+=1
        t=tk.Toplevel(self)
        t.wm_title("Supplier Window" + str(self.counter))
        l=tk.Label(t,text="This Is Inside Supplier")
        l.pack()


root=tk.Tk()
main=MainWindow(root)
main.pack()
root.mainloop()