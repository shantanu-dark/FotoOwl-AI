from pydantic import BaseModel, Field
from typing import List


class VideoIntent(BaseModel):
    pacing: str
    visual_style: str
    caption_tone: str
    transition_style: str


class ImageMetadata(BaseModel):
    image_name: str
    description: str
    emotion: str
    scene_type: str
    people_count: int
    importance_score: float
    quality_score: float
    story_relevance: float


class StoryboardScene(BaseModel):
    image_name: str
    duration: float
    caption: str
    transition: str
    animation: str


class Storyboard(BaseModel):
    scenes: List[StoryboardScene]


class CompileResult(BaseModel):
    success: bool
    error: str = ""