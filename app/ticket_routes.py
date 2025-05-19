from fastapi import APIRouter, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import Ticket, Priority
from app.database import cur, con

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/createticket", response_class=HTMLResponse)
async def create_ticket(request: Request):
    res = cur.execute(f"INSERT INTO tickets (ticket_info, priority) VALUES (?, ?)", (ticket.ticket_info, ticket.priority))
    return request

@router.get("/getticket", response_class=HTMLResponse)
async def get_ticket(ticket_id: int):
    res = cur.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
    return res.fetchone()

@router.get("/listtickets", response_class=HTMLResponse)
async def get_tickets():
    res = cur.execute("SELECT * FROM tickets")
    all_tickets = res.fetchall()
    return all_tickets

@router.delete("/deleteticket", response_class=HTMLResponse)
async def delete_ticket(ticket_id: int):
    res = cur.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))

