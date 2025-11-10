from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.utils.email_parser import parse_email
from app.models.lead import Lead
from app.utils.db import get_db

router = APIRouter()

@router.post("/webhook")
async def receive_lead(request: Request, db: Session = Depends(get_db)):
    payload = await request.json()
    
    subject = payload.get("subject", "")
    body_html = payload.get("body", "")
    sender = payload.get("from", "")
    platform = payload.get("source", "unknown")

    cleaned_text = parse_email(body_html)

    # Save to database
    new_lead = Lead(
        subject=subject,
        sender=sender,
        source=platform,
        text=cleaned_text
    )
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    return {"status": "ok", "lead_id": new_lead.id, "lead_text": cleaned_text}
