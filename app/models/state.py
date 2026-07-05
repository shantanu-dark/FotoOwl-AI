from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class PipelineState(BaseModel):
    """
    Shared state passed between all LangGraph agents.
    """

    # -------------------------
    # User Input
    # -------------------------
    image_paths: List[str] = Field(default_factory=list)
    user_prompt: str = ""

    # -------------------------
    # Intent Parser Output
    # -------------------------
    video_intent: Dict[str, Any] = Field(default_factory=dict)

    # -------------------------
    # Image Analyzer Output
    # -------------------------
    image_analysis: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------
    # Storyboard Output
    # -------------------------
    storyboard: List[Dict[str, Any]] = Field(default_factory=list)

    # -------------------------
    # Final Output
    # -------------------------
    output_video: Optional[str] = None