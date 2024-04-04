import sqlite3
import tkinter as tk 

def update(event):
    cur.execute(f'INSERT INTO HW_Database(name) VALUES(?)', [name.get()]);
    conn.commit()
    listing();
def get_list(conn):
    data = list(cur.execute ( 'SELECT ID, NAME FROM HW_Database'));
    return data;
def listing():
    name_list = get_list(cur);
    list_box = tk.Listbox();
    for i, n in name_list:
        list_box.insert(i, n);
    list_box.grid(row=3, column = 0, columnspan= 3);
dbFile = "//Users//lucas//Documents//Python //HW_Database.sqlite3"
conn = sqlite3.connect(dbFile);
cur = conn.cursor();
#cur.execute('CREATE TABLE HW_Database(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL)');
data = get_list(cur);
window = tk.Tk();
heading = tk.Label(text="Name ");
heading.grid(row=0, column= 0);
name = tk.Entry();
name.grid(row=0, column=1, columnspan =3);
enter = tk.Button(text="Submit");
#-1 left mouse, -3 right mouse
enter.bind('<Button-1>' , update);
enter.grid(row = 0, column = 0);
label = tk.Label(text='Roster: ');
label.grid(row=2, column=0);
listing();
window.mainloop();
cur.close();
