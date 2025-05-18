import sqlite3
from fastapi import FastAPI

app = FastAPI()

con = sqlite3.connect("tickets.db")
cur = con.cursor()
@app.get("/")
async def root():
    cur.execute("CREATE TABLE tickets(id, numbers)")
    return {"message":"Hello World"}

@app.post("/createticket")
async def create_ticket(value: str):
    res = cur.execute(f"INSERT INTO tickets VALUES (21 ,{value})")
    return res

@app.get("/getticket")
async def get_ticket(ticket_id: int):
    res = cur.execute("SELECT FROM tickets WHERE id=21")
    return res

@app.get("/listtickets")
async def get_tickets():
    res = cur.execute("SELECT * FROM tickets")
    return res

@app.delete("/deleteticket")
async def delete_ticket(ticket_id: int):
    pass
