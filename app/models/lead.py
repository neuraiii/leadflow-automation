from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.utils.db import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    sender = Column(String, index=True)
    source = Column(String, default="unknown")
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
