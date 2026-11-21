# python expense_trackerapi.py
#uvicorn expense_trackerapi:app --reload

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    title:str
    amount:float
    category:str

expenses =[]
@app.post("/expenses")
def track_expense(expense:Expense):
    expenses.append(expense)
    return {"message": "Expense added successfully!", "expense": expense}

@app.get("/expenses")
def expense_record():
    return{"Total item":len(expenses),"expenses":expenses}

