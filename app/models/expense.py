from pathlib import Path

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


def list_expenses():
    query = select(expenses).order_by(expenses.c.id)

    with engine.connect() as connection:
        rows = connection.execute(query).mappings()
        return [dict(row) for row in rows]