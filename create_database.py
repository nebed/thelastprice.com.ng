import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE visited_stores (id INTEGER PRIMARY KEY AUTOINCREMENT, store CHAR(30), url TEXT, times_visited REAL)')
print ("Table created successfully")
conn.close()