import json
import random
import os
import sys
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.sqlalchemy_models import Video

# Add the app directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def seed_new_mock_data_db():
    try:
        with open("C:\\Users\\Asus\\Desktop\\StreamFlix\\Frontend\\src\\data\\mockData.ts", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: mockData.ts not found. Please ensure the file exists at the specified path.")
        return

    declaration = "export const mockData: Movie[] = "
    declaration_start = content.find(declaration)
    if declaration_start == -1:
        print("Error: Could not find mockData declaration")
        return
        
    start = content.find("[", declaration_start + len(declaration))
    end = content.rfind("]")
    
    if start == -1 or end == -1:
        print("Error: Could not find the data array.")
        return
        
    json_data = content[start:end+1]

    try:
        movies_from_mock = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from mockData.ts: {e}")
        return

    db: Session = SessionLocal()
    try:
        for movie_data in movies_from_mock:
            # Generate missing data
            year = random.randint(2020, 2024)
            rating = random.choice(["PG", "PG-13", "R"])
            duration = f"{random.randint(1, 2)}h {random.randint(0, 59)}m"
            category = movie_data.get("subtitle", "General") # Use subtitle as category, or default
            
            # The 'thumb' is a relative path, create a placeholder full URL
            thumbnail_url = f"http://example.com/{movie_data.get('thumb', '')}"
            video_url = movie_data.get("sources", [""])[0] if movie_data.get("sources") else ""
            backdrop_url = thumbnail_url # Using thumbnail for backdrop as well

            # Try to find existing video by title
            db_video = db.query(Video).filter(Video.title == movie_data.get("title")).first()

            if db_video:
                # Update existing video
                db_video.description = movie_data.get("description")
                db_video.year = year
                db_video.rating = rating
                db_video.duration = duration
                db_video.category = category
                db_video.video_url = video_url
                db_video.thumbnail_url = thumbnail_url
                db_video.backdrop_url = backdrop_url
                print(f"Updated video: {movie_data.get('title')}")
            else:
                # Create new video
                new_video = Video(
                    title=movie_data.get("title"),
                    description=movie_data.get("description"),
                    year=year,
                    rating=rating,
                    duration=duration,
                    category=category,
                    video_url=video_url,
                    thumbnail_url=thumbnail_url,
                    backdrop_url=backdrop_url
                )
                db.add(new_video)
                print(f"Added new video: {movie_data.get('title')}")
        
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"An error occurred during seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_new_mock_data_db()
