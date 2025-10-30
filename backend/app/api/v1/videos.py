from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.sqlalchemy_models import Video
from app.schemas.pydantic_schemas import VideoCreate, VideoOut
from app.crud import crud_video

router = APIRouter(tags=["Videos"])

@router.post("/", response_model=VideoOut)
def create_video(video: VideoCreate, db: Session = Depends(get_db)):
    return crud_video.create_video(db=db, video=video)

@router.get("/", response_model=List[VideoOut])
def get_all_videos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    videos = crud_video.get_videos(db=db, skip=skip, limit=limit)
    return videos

@router.get("/search", response_model=List[VideoOut])
def search_videos(query: str = Query(..., min_length=1), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    videos = crud_video.search_videos(db=db, query=query, skip=skip, limit=limit)
    return videos

@router.get("/{video_id}", response_model=VideoOut)
def get_video(video_id: int, db: Session = Depends(get_db)):
    video = crud_video.get_video(db=db, video_id=video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video