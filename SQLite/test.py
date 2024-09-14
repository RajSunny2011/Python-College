import sqlite3

conn = sqlite3.connect("test.db")
print(conn)
conn.close()

with sqlite3.connect("test1.db") as conn:
    print(conn)
