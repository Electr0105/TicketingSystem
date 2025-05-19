from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app import ticket_routes

app = FastAPI()
app.include_router(ticket_routes.router)
templates = Jinja2Templates(directory="app/templates")
