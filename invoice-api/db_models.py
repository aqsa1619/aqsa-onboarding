from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from db import Base


class InvoiceRow(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)  # primary key
    client: Mapped[str]
    amount: Mapped[float]
    due_date: Mapped[date]
    paid: Mapped[bool] = mapped_column(default=False)