import json
import os

from app.services.llm import llm
from app.services.vector_store import retrieve
from app.config import Config


class ScriptGeneratorAgent:

    def __call__(self, state):

        print("\nGenerating Remotion Script...\n")

        with open(
            os.path.join(
                Config.OUTPUT_FOLDER,
                "storyboard.json"
            ),
            "r",
            encoding="utf-8"
        ) as f:

            storyboard = json.load(f)

        docs = retrieve(
            "How to create a Remotion slideshow with captions"
        )

        prompt = f"""
You are an expert React + Remotion developer.

Use the Remotion documentation below.

{docs}

Storyboard

{json.dumps(storyboard, indent=2)}

Generate ONE React component.

Requirements:

- React
- Remotion
- AbsoluteFill
- Sequence
- Img
- Caption
- export default

Return ONLY code.
"""

        code = llm.generate_text(prompt)

        os.makedirs(
            Config.OUTPUT_FOLDER,
            exist_ok=True
        )

        output = os.path.join(
            Config.OUTPUT_FOLDER,
            "generated_video.tsx"
        )

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(code)

        state.remotion_script = output

        print("✅ React Component Generated")

        return state