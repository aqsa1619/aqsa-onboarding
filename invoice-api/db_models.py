from datetime import date, datetime, timezone

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class InvoiceRow(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)
    client: Mapped[str]
    amount: Mapped[float]
    due_date: Mapped[date]
    paid: Mapped[bool] = mapped_column(default=False)


class UserRow(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    role: Mapped[str] = mapped_column(default="editor")


class JobRow(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(default="queued")   # queued / running / done / failed
    result: Mapped[str | None] = mapped_column(Text)        # the report, saved as JSON text
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))  # who asked for it
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )