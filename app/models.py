from enum import Enum
from pydantic import BaseModel

class Priority(Enum):
    MINOR = 1
    MAJOR = 2
    CATASTROPHIC = 3

class Ticket(BaseModel):
    ticket_info: str
    priority: Priority
