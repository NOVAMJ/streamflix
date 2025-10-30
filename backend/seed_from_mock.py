
import json
import os
import re
import sys
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.sqlalchemy_models import Video

# Add the app directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def seed_videos_from_mock(db: Session):
    with open(os.path.join(os.path.dirname(__file__), '..\..\Frontend\src\data\mockData.ts'), 'r', encoding='utf-8') as f:
        content = f.read()

    # Use regex to find all movie objects
    movie_objects = re.findall(r'(?<!interface Movie )({\s*id:[^}]*title:[^}]*})', content)

    all_movies = []
    for movie_object_str in movie_objects:
        movie = {}
        for line in movie_object_str.split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                # remove trailing comma
                if value.endswith(','):
                    value = value[:-1]
                # remove quotes
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                if value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]

                if key == 'genre':
                    value = [g.strip().replace("'", "").replace("\"", "") for g in value[1:-1].split(',')]
                
                movie[key] = value
        all_movies.append(movie)

    for movie in all_movies:
        db_video = Video(
            id=int(movie['id']),
            title=movie['title'],
            description=movie['description'],
            year=int(movie['year']),
            rating=movie['rating'],
            duration=movie['duration'],
            category=','.join(movie['genre']),
            video_url=f"https://videos.pexels.com/video-files/{movie['id']}.mp4",  # Using backdrop as video_url for now
            thumbnail_url=movie['thumbnail'],
            backdrop_url=movie['backdrop']
        )
        db.merge(db_video)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_videos_from_mock(db)
        print("Successfully seeded videos from mock data.")
    finally:
        db.close()
