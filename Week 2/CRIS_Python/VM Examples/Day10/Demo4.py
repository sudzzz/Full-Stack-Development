#how to open different window from main window
import tkinter as tk
class MainWindow(tk.Frame):
    counter=0
    def __init__(self,mst):
        tk.Frame.__init__(self,mst)
        self.bt1=tk.Button(self,text="Supplier",
                              command=self.create_win)
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