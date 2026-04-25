"""
routes/videos.py — REST endpoints for videos.

GET /api/videos              → all videos
GET /api/videos/{id}         → single video
"""

from fastapi import APIRouter, HTTPException

from backend.models import Video
from backend.data.videos import ALL_VIDEOS

router = APIRouter(tags=["Videos"])


@router.get("/videos", response_model=list[Video])
def get_videos():
    """Return all videos."""
    return ALL_VIDEOS


@router.get("/videos/{video_id}", response_model=Video)
def get_video(video_id: str):
    """Return a single video by its ID."""
    for video in ALL_VIDEOS:
        if video.id == video_id:
            return video
    raise HTTPException(status_code=404, detail=f"Video '{video_id}' not found.")
