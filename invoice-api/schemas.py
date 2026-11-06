from datetime import date
from pydantic import BaseModel, ConfigDict, Field


class InvoiceIn(BaseModel):
    client: str = Field(min_length=1)
    amount: float = Field(gt=0)
    due_date: date
    paid: bool = False


class InvoiceOut(InvoiceIn):
    model_config = ConfigDict(from_attributes=True)
    id: int

class LoginIn(BaseModel):
    email: str
    password: str