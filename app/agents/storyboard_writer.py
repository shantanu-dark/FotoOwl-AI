import json
import os

from app.services.llm import llm
from app.services.vector_store import retrieve
from app.config import Config


class StoryboardWriterAgent:

    def __call__(self, state):

        # Top 10 ranked images
        top_images = state.image_analysis[:10]

        # -----------------------------
        # RAG Retrieval
        # -----------------------------
        rag_docs = retrieve(state.user_prompt)

        rag_context = "\n\n".join(rag_docs)

        print("\n📚 Retrieved Knowledge:\n")
        print(rag_context)

        # -----------------------------
        # Prompt
        # -----------------------------
        prompt = f"""
You are an expert cinematic wedding video editor.

Use the following editing knowledge while creating the storyboard.

Editing Knowledge:

{rag_context}

------------------------------------------------

User Request:

{state.user_prompt}

------------------------------------------------

Available Images:

{json.dumps(top_images, indent=2)}

------------------------------------------------

Create a cinematic storyboard.

Return ONLY valid JSON.

Format:

[
    {{
        "image":"filename.jpg",
        "caption":"",
        "duration":3,
        "transition":"",
        "animation":""
    }}
]

Rules:

- Use each image only once.
- Every image must have a caption.
- Caption should be emotional.
- Caption length between 3 and 8 words.
- Duration between 2 and 4 seconds.
- Transition: fade, dissolve or slide.
- Animation: zoom-in, zoom-out or pan.
- Follow the retrieved editing knowledge whenever applicable.
- Return ONLY valid JSON.
"""

        storyboard_text = llm.generate_text(prompt)

        storyboard = json.loads(storyboard_text)

        # -----------------------------
        # Save Storyboard
        # -----------------------------
        os.makedirs(
            Config.OUTPUT_FOLDER,
            exist_ok=True
        )

        with open(
            os.path.join(
                Config.OUTPUT_FOLDER,
                "storyboard.json"
            ),
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                storyboard,
                f,
                indent=4
            )

        state.storyboard = storyboard

        print("\n✅ Storyboard Created")

        return state