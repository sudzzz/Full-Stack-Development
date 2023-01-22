#Layout Management:
'''
Pack-we dont need precise location but
we can declare the positions of controls
relative to each other...

Grid
Place
'''

#Use of Pack based Layout Management

from tkinter import *
root=Tk()

Label(root,text="India",bg="red",fg="white").pack(fill=X,padx=10,pady=20,side=LEFT)
Label(root,text="Australia",bg="green",fg="white").pack(fill=X,padx=10,pady=20,side=RIGHT)
Label(root,text="Pakistan",bg="blue",fg="white").pack(fill=X,padx=10,pady=20,side=LEFT)

'''
lbl=Label(root,text="Pakistan",bg="blue",fg="white")
lbl.pack(fill=X)
'''

mainloop()