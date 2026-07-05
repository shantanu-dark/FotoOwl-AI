import json
import os
import shutil

from app.services.timeline import TimelineGenerator
from app.services.remotion import RemotionRenderer


class RenderAgent:

    def __call__(self, state):

        print("\nPreparing Remotion Assets...\n")

        # --------------------------------------------------
        # Create Timeline
        # --------------------------------------------------

        timeline = TimelineGenerator.generate()

        os.makedirs(
            "remotion/public/data",
            exist_ok=True
        )

        with open(
            "remotion/public/data/timeline.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                timeline,
                f,
                indent=4
            )

        # --------------------------------------------------
        # Copy Images
        # --------------------------------------------------

        image_folder = "remotion/public/images"

        os.makedirs(
            image_folder,
            exist_ok=True
        )

        # Clean old images
        for file in os.listdir(image_folder):
            file_path = os.path.join(image_folder, file)

            if os.path.isfile(file_path):
                os.remove(file_path)

        # Copy new images
        for image in state.image_paths:

            shutil.copy2(
                image,
                os.path.join(
                    image_folder,
                    os.path.basename(image)
                )
            )

        print("✅ Assets Prepared")

        # --------------------------------------------------
        # Render Video
        # --------------------------------------------------

        print("\nRendering Video...\n")

        result = RemotionRenderer.render()

        if result.returncode == 0:

            print("\n✅ Video Rendered Successfully!")

            state.output_video = os.path.abspath(
                "output/final_video.mp4"
            )

        else:

            print("\n❌ Rendering Failed")

            print(result.stderr)

            state.output_video = None

        return state