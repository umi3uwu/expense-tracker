from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel

from app.models import expense as models
from app.views.expense import ExpenseView


router = APIRouter(prefix="/expenses")


class ExpenseBody(BaseModel):
    amount: int
    date: date
    category: str
    source: str
    note: str | None = None

@router.get("", response_model=list[ExpenseView])
def list_expenses(
    category: str | None = None,
    source: str | None = None,
    date_from: date | None = None,
    date_to: date | None = None

):
    return models.list_expenses(
        category, source, date_from, date_to
    )

@router.post("", response_model=ExpenseView)
def create_expense(body: ExpenseBody):
    return models.create_expense(
        body.amount,
        body.date,
        body.category,
        body.source,
        body.note
    )