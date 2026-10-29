from datetime import date

from pydantic import BaseModel


class ExpenseView(BaseModel):
    id: int
    amount: int
    date: date
    category: str
    source: str
    note: str | None = None