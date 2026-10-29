from fastapi import FastAPI

from app.controllers.expense import router
from app.models.expense import initialize_database


initialize_database()

app = FastAPI(title="Expense Tracker")
app.include_router(router)