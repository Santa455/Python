import sqlite3
##print("records:\n", records)

dbFile = "//Users//lucas//Documents//Python //HW_SQL.sqlite3"
##dbFile =  "HW_SQL.sqlite3"

conn = sqlite3.connect(dbFile);
##dbFile = "//Users//lucas//Documents//Python //HW_SQL.sqlite3"
cur = conn.cursor()

cur.execute("DELETE FROM dataset WHERE Score < 740;")
cur.execute("SELECT * FROM dataset;")
records = cur.fetchall()


for record in records: 
    print("Result: ", record)