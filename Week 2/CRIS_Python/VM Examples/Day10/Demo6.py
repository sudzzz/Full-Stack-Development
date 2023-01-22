from tkinter import *

countries=['india','australia','pakistan']

rw=0
for c in countries:
  Label(text=c).grid(row=rw,column=0)
  Text(height=2,width=10).grid(row=rw,column=1)
  rw+=1

mainloop()