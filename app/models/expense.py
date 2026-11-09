from pathlib import Path
from datetime import date, timedelta
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, create_engine, select

database_path = Path(__file__).resolve().parents[2] / "expenses.db"
engine = create_engine(f"sqlite:///{database_path}")

metadata = MetaData()

expenses = Table(
    "expenses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("amount", Integer, nullable=False),
    Column("date", Date, nullable=False),
    Column("category", String, nullable=False),
    Column("source", String, nullable=False),
    Column("note", String, nullable=True),
)


def initialize_database():
    metadata.create_all(engine)


def list_expenses(
        category: str | None = None,
        source: str | None = None,
        date_from: date | None = None,
        date_to: date | None = None
):
    query = select(expenses)

    if category is not None:
        query = query.where(expenses.c.category == category)

    if source is not None:
        query = query.where(expenses.c.source == source)

    if date_from is not None:
        query = query.where(expenses.c.date >= date_from)
    if date_to is not None:
        query = query.where(expenses.c.date <= date_to)

    query = query.order_by(expenses.c.id)

    with engine.connect() as connection:
        rows = connection.execute(query).mappings()
        return [dict(row) for row in rows]

def create_expense(
        amount:int,
        expense_date: date,
        category: str,
        source: str,
        note: str | None
):
    query = expenses.insert().values(
        amount = amount,
        date = expense_date,
        category = category,
        source = source,
        note = note
    )

    with engine.begin() as connection:
        result = connection.execute(query)
        expense_id = result.inserted_primary_key[0]

        return{
            "id": expense_id,
            "amount":amount,
            "date":expense_date,
            "category": category,
            "source": source,
            "note":note
        }

def update_expense(expense_id: int, values: dict):
    query=(
        expenses.update()
        .where(expenses.c.id == expense_id)
        .values(**values)
    )

    with engine.begin() as connection:
        result = connection.execute(query)

        if result.rowcount ==0:
            return None

        select_query = select(expenses).where(expenses.c.id == expense_id)
        row = connection.execute(select_query).mappings().first()

        return dict(row)

def delete_expense(expense_id: int):
    query=expenses.delete().where(expenses.c.id == expense_id)

    with engine.begin() as connection:
        result = connection.execute(query)

        return result.rowcount>0

def get_summary(
        period: str | None = None,
        date_from: date | None = None,
        date_to: date | None = None
):
    today=date.today()

    if period=="today":
        date_from=today
        date_to=today

    elif period=="week":
        date_from=today-timedelta(days=6)
        date_to=today

    elif period == "month":
        date_from = today- timedelta(days=29)
        date_to = today

    rows = list_expenses(
        date_from = date_from,
        date_to = date_to
    )

    total_amount = sum(row["amount"] for row in rows)
    count = len(rows)

    return{
        "total_amount": total_amount,
        "count": count
    }