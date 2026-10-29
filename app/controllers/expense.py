from fastapi import APIRouter

from app.models import expense as models
from app.views.expense import ExpenseView


router = APIRouter(prefix="/expenses")


@router.get("", response_model=list[ExpenseView])
def list_expenses():
    return models.list_expenses()