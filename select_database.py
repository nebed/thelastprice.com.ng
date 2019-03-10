import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT id, store, url, times_visited from visited_stores")
for row in cursor:
   print ("ID = ", row[0])
   print ("STORE = ", row[1])
   print ("URL = ", row[2])
   print ("TIMES_VISITED = ", row[3], "\n")

print ("Operation done successfully")
conn.close()