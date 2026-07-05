import os

from app.graph.workflow import build_graph
from app.models.state import PipelineState


IMAGE_FOLDER = "data/images"

image_paths = []

if os.path.exists(IMAGE_FOLDER):

    for file in os.listdir(IMAGE_FOLDER):

        if file.lower().endswith((".jpg", ".jpeg", ".png")):

            image_paths.append(
                os.path.join(
                    IMAGE_FOLDER,
                    file
                )
            )


graph = build_graph()


state = PipelineState(

    image_paths=image_paths,

    user_prompt="""
Cinematic wedding reel

Warm colors

Slow motion

Minimal captions

Emotional storytelling
"""
)


result = graph.invoke(state)

print(result)