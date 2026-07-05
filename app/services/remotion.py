import subprocess
import os


class RemotionRenderer:

    @staticmethod
    def render():

        output_path = os.path.abspath("output/final_video.mp4")

        command = [
            "npx.cmd",
            "remotion",
            "render",
            "WeddingVideo",
            output_path
        ]

        result = subprocess.run(
            command,
            cwd="remotion",
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.stderr:
            print(result.stderr)

        return result