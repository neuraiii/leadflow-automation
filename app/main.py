from fastapi import FastAPI
from app.routes import webhook

app = FastAPI(title="Lead Ingestion Service")

# Include router
app.include_router(webhook.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Lead automation service running"}
