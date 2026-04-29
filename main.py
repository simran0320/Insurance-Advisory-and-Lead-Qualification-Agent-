from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

FILE_PATH = "leads.xlsx"

from typing import Optional, List

class Lead(BaseModel):
    lead_id: Optional[str] = None
    call_date: Optional[str] = None
    call_duration_seconds: Optional[int] = None
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    age: Optional[str] = None
    dependents: Optional[str] = None
    existing_coverage: Optional[str] = None
    existing_coverage_details: Optional[str] = None
    employment_type: Optional[str] = None
    smoker: Optional[str] = None
    lead_classification: Optional[str] = None
    engagement_notes: Optional[str] = None
    hook_for_advisor: Optional[str] = None
    callback_confirmed: Optional[bool] = None
    callback_date: Optional[str] = None
    callback_time: Optional[str] = None
    crosssell_interest: Optional[List[str]] = []
    call_outcome: Optional[str] = None
    call_summary: Optional[str] = None


@app.post("/save-lead")
def save_lead(lead: Lead):
    data = lead.dict()

    df = pd.DataFrame([data])

    if os.path.exists(FILE_PATH):
        existing = pd.read_excel(FILE_PATH)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_excel(FILE_PATH, index=False)

    return {"status": "saved"}
