import pathlib
from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox

import sqlite3;
import pathlib;

root = Tk();
root.title("Final part 3");
root.geometry("1000x450");

averageRunTime = 0.0

dbFile = pathlib.Path("FinalExamDatabase.sqlite3");
connection = sqlite3.connect(dbFile);
command = connection.cursor();

def fnDisplayValues():
    library.delete(0, END)
    command.execute("SELECT textValue, numericValue FROM examData");
    records = command.fetchall();
    for i in records:
        library.insert(END, i[0]);
    calcAverageTime();



def calcAverageTime():
    global averageRunTime;
    ballon = command.execute("SELECT numericValue FROM examData");
    ballonLife  = ballon.fetchall();
    sum = 0;

    for t in ballonLife:
        sum = sum += t;
    avg = sum / len(ballonLife);
    averageRunTime = avg;
    lblAvgTime.config(text = averageRunTime);
#def calcAverageTime():
   # global averageRunTime;
   # averageRunTime = 0
   # avg = command.execute("SELECT AVG(numericValue) FROM examData");

  #  lblAvgTime.config(text = avg);
  #  return;


def fnAddName():
    runTime();
    command.execute("INSERT INTO examData (textValue, numericValue) VALUES (' " + valueName.get() + " ' , ' " + valueTime.get() + " ') ");
    connection.commit();

    fnDisplayValues();

def runTime():
    while True:
        amount = valueTime.get()
        try:
            val = int(amount)
            if val >=0:
                break
            else :
                messagebox.showerror('Error','Run time must be a value greater than zero.')
                break
        except ValueError:
            messagebox.showerror('Error','Must be a number')
            break
    return val;

            


lblMovie = Label(root, text = 'Add Movie: ');
lblMovie.grid(row = 0, column = 0, sticky = W);

lblTitle = Label(root, text = 'Movie Title: ');
lblTitle.grid(row = 1, column = 0, columnspan = 2, sticky = W);

valueName = Entry(root);
valueName.grid(row= 1, column =1, sticky = W);

lblTime = Label(root, text= 'Run Time: ');
lblTime.grid(row = 2, column = 0, sticky = W);

valueTime = Entry(root);
valueTime.grid(row = 2, column =1, sticky = W);

submit = Button(root, text="Submit", command=fnAddName);
submit.grid(row=3, column=0, sticky=W);

###
lblLibrary = Label(root, text = 'Movie Library: ');
lblLibrary.grid(row= 0 , column = 3, sticky = W);

libraryFrame = Frame(root);
libraryFrame.grid(row = 1, column = 3, columnspan = 2);

scrollbar = Scrollbar(libraryFrame);
scrollbar.pack(side=RIGHT, fill=Y);
library = Listbox(libraryFrame, height=5, width=20, yscrollcommand=scrollbar.set);
library.pack()
scrollbar.config(command=library.yview);

lblAvgRT = Label(root, text = 'Average Run Time: ');
lblAvgRT.grid(row= 2, column = 3, sticky = W);

lblAvgTime = Label(root, text = averageRunTime);
lblAvgTime.grid(row= 2, column = 4, sticky = W);

fnDisplayValues();

root.mainloop();