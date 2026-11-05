from datetime import date as DateType

from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

from app.models import expense as models
from app.views.expense import ExpenseView


router = APIRouter(prefix="/expenses")


class ExpenseBody(BaseModel):
    amount: int
    date: DateType
    category: str
    source: str
    note: str | None = None

class ExpenseUpdateBody(BaseModel):
    amount: int | None = None
    date: DateType | None = None
    category: str | None = None
    source: str | None = None
    note: str | None = None


@router.get("", response_model=list[ExpenseView])
def list_expenses(
    category: str | None = None,
    source: str | None = None,
    date_from: DateType | None = None,
    date_to: DateType | None = None

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

@router.patch("/{id}", response_model=ExpenseView)
def update_expense(id: int, body: ExpenseUpdateBody):
    expense = models.update_expense(
        id,
        body.model_dump(exclude_unset=True)
    )

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )
    return expense

@router.delete("/{id}")
def delete_expense(id:int):
    deleted=models.delete_expense(id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return{"deleted": True}