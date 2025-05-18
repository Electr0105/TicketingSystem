from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/createticket")
async def create_ticket():
    pass

@app.get("/getticket")
async def get_ticket(ticket_id: int):
    pass

@app.get("/gettickets")
async def get_tickets():
    pass

@app.delete("/deleteticket")
async def delete_ticket(ticket_id: int):
    pass
