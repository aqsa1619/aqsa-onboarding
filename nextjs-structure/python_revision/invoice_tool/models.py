
from dataclasses import dataclass
from datetime import date


@dataclass
class Invoice:
    client: str
    amount: float
    due_date: date
    paid: bool = False

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Invoice amount must be greater than zero")

        if not self.client.strip():
            raise ValueError("Client name cannot be empty")
