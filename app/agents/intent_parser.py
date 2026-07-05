from app.models.schemas import VideoIntent
from app.services.llm import llm


class IntentParserAgent:

    def __call__(self, state):

        prompt = f"""

Convert the following user request into JSON.

User Prompt:

{state.user_prompt}

Extract:

- pacing
- visual_style
- caption_tone
- transition_style

"""

        intent = llm.generate_json(
            prompt,
            VideoIntent
        )

        state.video_intent = intent

        print("\n✅ Video Intent")
        print(state.video_intent)

        return state