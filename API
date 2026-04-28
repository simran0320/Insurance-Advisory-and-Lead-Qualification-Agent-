from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

FILE_PATH = "leads.xlsx"

class Lead(BaseModel):
    lead_id: str
    call_date: str
    call_duration_seconds: int
    customer_name: str
    customer_phone: str
    age: str
    dependents: str
    existing_coverage: str
    existing_coverage_details: str
    employment_type: str
    smoker: str
    lead_classification: str
    engagement_notes: str
    hook_for_advisor: str
    callback_confirmed: bool
    callback_date: str
    callback_time: str
    crosssell_interest: list
    call_outcome: str
    call_summary: str

@app.post("/save-lead")
def save_lead(lead: Lead):
    data = lead.dict()

    df = pd.DataFrame([data])

    if os.path.exists(FILE_PATH):
        existing = pd.read_excel(FILE_PATH)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_excel(FILE_PATH, index=False)

    return {"status": "saved"}
