from datetime import date

from pydantic import BaseModel, Field


class InvoiceIn(BaseModel):
    client: str = Field(min_length=1)
    amount: float = Field(gt=0)
    due_date: date


class InvoiceOut(InvoiceIn):
    id: int
    paid: bool = False