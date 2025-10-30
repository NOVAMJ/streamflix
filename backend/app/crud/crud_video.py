from sqlalchemy.orm import Session
from app.models.sqlalchemy_models import Video
from app.schemas.pydantic_schemas import VideoCreate

def get_video(db: Session, video_id: int):
    return db.query(Video).filter(Video.id == video_id).first()

def get_videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Video).offset(skip).limit(limit).all()

def create_video(db: Session, video: VideoCreate):
    db_video = Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def search_videos(db: Session, query: str, skip: int = 0, limit: int = 100):
    return db.query(Video).filter(Video.title.contains(query)).offset(skip).limit(limit).all()