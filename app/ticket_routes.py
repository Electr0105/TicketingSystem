from fastapi import APIRouter, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import Ticket, Priority
from app.database import cur, con

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    res = cur.execute("SELECT * FROM tickets")
    tickets = res.fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "tickets": tickets})

@router.get("/tickets", response_class=HTMLResponse)
async def tickets(request: Request):
    tickets = cur.execute("SELECT * FROM tickets").fetchall()
    return templates.TemplateResponse("tickets.html", {"request": request, "tickets": tickets})

@router.post("/createticket", response_class=HTMLResponse)
async def create_ticket(ticket_title: str = Form(...), ticket_body: str = Form(...), priority: str = Form(...)):
    res = cur.execute(f"INSERT INTO tickets (ticket_title, ticket_body, priority) VALUES (?, ?, ?)", (ticket_title, ticket_body, priority))
    return HTMLResponse("<p>Ticket Created</p>")

@router.get("/ticket-form", response_class=HTMLResponse)
async def ticket_form(request: Request):
    return templates.TemplateResponse("create-ticket.html", {"request": request})

@router.get("/getticket")
async def get_ticket(ticket_id: int):
    res = cur.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
    return res.fetchone()

@router.get("/listtickets")
async def get_tickets():
    res = cur.execute("SELECT * FROM tickets")
    all_tickets = res.fetchall()
    return all_tickets

@router.delete("/deleteticket")
async def delete_ticket(ticket_id: int):
    res = cur.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))

