import sqlite3

con = sqlite3.connect("ticketingDatabase.db", check_same_thread=False)
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, ticket_info TEXT, priority TEXT)")

con.commit()

