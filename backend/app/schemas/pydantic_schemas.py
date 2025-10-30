from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class VideoBase(BaseModel):
    title: str
    description: str
    year: int
    rating: str
    duration: str
    category: str
    video_url: str # Added video_url
    thumbnail_url: str
    backdrop_url: str

class VideoCreate(VideoBase):
    pass

class VideoOut(VideoBase):
    id: int

    class Config:
        from_attributes = True
