from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_video():
    return {"message": "Upload successful"}
