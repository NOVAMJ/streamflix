from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def create_admin():
    db = SessionLocal()
    admin_email = "admin@netflixclone.com"
    admin_username = "admin"
    admin_password = "admin123"

    existing = db.query(User).filter(User.email == admin_email).first()
    if existing:
        print("✅ Admin already exists.")
        return

    admin_user = User(
        email=admin_email,
        username=admin_username,
        hashed_password=get_password_hash(admin_password),
        is_active=True,
        is_admin=True
    )

    db.add(admin_user)
    db.commit()
    print("✅ Admin user created successfully!")
    print(f"Email: {admin_email}")
    print(f"Password: {admin_password}")

if __name__ == "__main__":
    create_admin()
