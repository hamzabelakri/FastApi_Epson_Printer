from pydantic import BaseModel
from datetime import datetime

class Ticket_Base_Model(BaseModel):
    receipt_id: int
    payment_date: str
    entry_date: str
    ticket_id: int
    epan: str
    length_of_stay: str
    parking_fees: float
    vat_percentage: float
    vat_amount: float
    total_amount: float