from datetime import date
from pydantic import BaseModel, Field


class InvoiceIn(BaseModel):
    client: str = Field(min_length=1)
    amount: float = Field(gt=0)
    due_date: date
    paid: bool = False  # <-- Add this line here!


class InvoiceOut(InvoiceIn):
    id: int