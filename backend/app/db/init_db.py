from app.db.database import engine
from app.db.base import Base
from app.models import user

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
