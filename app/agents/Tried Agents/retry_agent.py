import os

from app.services.llm import llm
from app.config import Config


class RetryAgent:

    def __call__(self, state):

        if state.compile_success:

            return state

        print("\nRetry Agent Fixing Code...\n")

        path = os.path.join(
            Config.OUTPUT_FOLDER,
            "generated_video.tsx"
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            code = f.read()

        prompt = f"""
You are an expert React + TypeScript developer.

The following code does not compile.

Compiler Error:

{state.compile_error}

React Code:

{code}

Return ONLY corrected code.

Do not explain anything.
"""

        fixed_code = llm.generate_text(prompt)

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(fixed_code)

        state.retry_count += 1

        print("✅ Retry Complete")

        return state