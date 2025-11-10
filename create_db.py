from app.utils.db import engine, Base
from app.models.lead import Lead

Base.metadata.create_all(bind=engine)
print("Database and tables created!")

