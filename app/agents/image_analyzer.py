import json
import os

from app.utils.image_utils import image_score
from app.config import Config


class ImageAnalyzerAgent:

    def __call__(self, state):

        analysis = []

        print("\nAnalyzing Images...\n")

        for image_path in state.image_paths:

            result = image_score(image_path)

            if result:

                analysis.append(result)

        analysis.sort(
            key=lambda x: x["importance_score"],
            reverse=True
        )

        state.image_analysis = analysis

        os.makedirs(Config.OUTPUT_FOLDER, exist_ok=True)

        with open(
            os.path.join(
                Config.OUTPUT_FOLDER,
                "image_analysis.json"
            ),
            "w"
        ) as f:

            json.dump(
                analysis,
                f,
                indent=4
            )

        print("\nTop 10 Images\n")

        for img in analysis[:10]:

            print(
                f'{img["image_name"]} -> {img["importance_score"]}'
            )

        return state