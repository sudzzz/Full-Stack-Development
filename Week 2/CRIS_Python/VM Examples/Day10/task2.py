import tkinter as tk

class Example(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)

        # add bindings to a new tag that we're going to be using
        self.bind_class("t", "<Enter>", self.on_enter)
        self.bind_class("t", "<Leave>", self.on_leave)
        self.bind_class("t", "<Button-1>", self.on_click)

        # create some widgets and give them this tag
        for i in range(5):
            l = tk.Label(self, text="Button #%s" % i, background="white")
            l.pack(side="top")
            new_tags = l.bindtags() + ("t",)
            l.bindtags(new_tags)

    def on_enter(self, event):
        event.widget.configure(background="bisque")

    def on_click(self, event):
        print(self)
        event.widget.configure(background="red")

    def on_leave(self, event):
        event.widget.configure(background="white")

if __name__ == "__main__":
    root = tk.Tk()
    view = Example()
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()