import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from app.db.database import engine

# Load the .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL",None)
print("🔍 DATABASE_URL =", DATABASE_URL)  # TEMP for debugging

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found. Check your .env file or environment variables.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
