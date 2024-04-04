#Imports
from tkinter import *
import random 

#Functions
def cmdClickHERE():
    lblOutput.config(text="Jane, Doe")
def cmdClickHERE1():
    lblOutput1.config(text="Doe, Jane")
def cmdClickHERE2():
    lblOutput2.config(text="Jane")
def cmdClickHERE3():
    lblOutput3.config(text="Doe")
def cmdClickHERE4():
    lblOutput.config(text="******")
    lblOutput1.config(text="******")
    lblOutput2.config(text="")
    lblOutput3.config(text="")

#Calling tkinker
root = Tk() 

#Window
root.title("Names Format")
root.geometry("400x200")

#Buttons
btnClickHERE = Button(root, text="First Last" , command=cmdClickHERE)
btnClickHERE.grid(row=0, column=0)

btnClickHere1 = Button(root, text="Last, First", command=cmdClickHERE1)
btnClickHere1.grid(row=1, column= 0)

btnClickHere2 = Button(root, text="First", command=cmdClickHERE2)
btnClickHere2.grid(row=2, column= 0)

btnClickHere3 = Button(root, text="Last", command=cmdClickHERE3)
btnClickHere3.grid(row=3, column= 0)

btnClickHere4 = Button(root, text="RESET", command=cmdClickHERE4)
btnClickHere4.grid(row=4, column= 0)

#Outputs
lblOutput = Label(root, text="******")
lblOutput.grid(row=0, column=1)

lblOutput1 = Label(root, text="******")
lblOutput1.grid(row=1, column=1)

lblOutput2 = Label(root)
lblOutput2.grid(row=2, column=1)

lblOutput3 = Label(root)
lblOutput3.grid(row=3, column=1)

#Recurring
root.mainloop()
