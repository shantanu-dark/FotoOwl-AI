import os
import subprocess

from app.config import Config


class CompilerAgent:

    def __call__(self, state):

        print("\nChecking Generated React Component...\n")

        script_path = os.path.join(
            Config.OUTPUT_FOLDER,
            "generated_video.tsx"
        )

        if not os.path.exists(script_path):

            state.compile_success = False
            state.compile_error = "generated_video.tsx not found"

            return state

        try:

            result = subprocess.run(

                [
                    "npx",
                    "tsc",
                    "--noEmit",
                    script_path
                ],

                capture_output=True,
                text=True

            )

            if result.returncode == 0:

                print("✅ Compilation Successful")

                state.compile_success = True
                state.compile_error = ""

            else:

                print("❌ Compilation Failed")

                state.compile_success = False
                state.compile_error = result.stderr

        except Exception as e:

            state.compile_success = False
            state.compile_error = str(e)

        return state