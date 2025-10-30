from fastapi import FastAPI
from app.api.v1 import auth, users, videos, admin
from app.db.database import engine
from app.models.sqlalchemy_models import User,Base  # Import your models
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Create all tables
# print("Dropping all tables...")
# Base.metadata.drop_all(bind=engine)

# print("Recreating tables...")
# Base.metadata.create_all(bind=engine)

# print("✅ Tables recreated successfully!")


app = FastAPI(title="Netflix Clone API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="C:/Users/Asus/Desktop/StreamFlix/static"), name="static")

app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(videos.router, prefix="/api/v1/videos", tags=["videos"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])

@app.get("/")
def root():
    return {"message": "Welcome to Netflix Clone Backend"}


# from app.db.database import Base, engine
# from app.models.user import User

# Base.metadata.create_all(bind=engine)
