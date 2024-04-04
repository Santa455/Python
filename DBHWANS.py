# Libraries for Database
import sqlite3
import pathlib
# Variables/Objects for Database
dbFile = pathlib.Path("PATH TO DATABASE FILE/HW_Database.sqlite3")
connection = sqlite3.connect(dbFile)
command = connection.cursor()
def fnDisplayValues():
    #Clear the current output
    roster.delete(0,END)
    #Get data from database
    command.execute("SELECT name FROM HW_Database")
    records = command.fetchall()
    for row in records:
        roster.insert(END, row[0])
def fnAddName():
    command.execute("INSERT INTO HW_Database (name) VALUES ('" + value.get() + "')")
    connection.commit()
    fnDisplayValues()
# UI

from tkinter import *

root = Tk()
root.title("HW-Database")
root.geometry("300x180")
label1 = Label(root, text="Name:")
label1.grid(row=0, column=0, sticky=W)
value = Entry(root)
value.grid(row=0, column=1, sticky=W)
submit = Button(root, text="Submit", command=fnAddName)
submit.grid(row=0, column=2, sticky=W)
label2 = Label(root, text="Roster:")
label2.grid(row=1, column=0, sticky=W)
rosterFrame = Frame(root)
rosterFrame.grid(row=2, column=0, columnspan=2, sticky=W)
scrollbar = Scrollbar(rosterFrame)
scrollbar.pack(side=RIGHT, fill=Y)
roster = Listbox(rosterFrame, height=5, width=30, yscrollcommand=scrollbar.set)
roster.pack()
scrollbar.config(command=roster.yview)
#fnDisplayValues()
root.mainloop()