import json
import os

from app.config import Config


class TimelineGenerator:

    @staticmethod
    def generate():

        storyboard_path = os.path.join(
            Config.OUTPUT_FOLDER,
            "storyboard.json"
        )

        with open(
            storyboard_path,
            "r",
            encoding="utf-8"
        ) as f:

            storyboard = json.load(f)

        timeline = []

        current_frame = 0
        fps = 30

        for scene in storyboard:

            duration_frames = scene["duration"] * fps

            timeline.append({

                "image": scene["image"],

                "caption": scene["caption"],

                "from": current_frame,

                "duration": duration_frames,

                "animation": scene["animation"],

                "transition": scene["transition"]

            })

            current_frame += duration_frames

        return timeline