import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    IMAGE_FOLDER = "data/images"
    OUTPUT_FOLDER = "output"

    MAX_RETRIES = 3

    OPENAI_MODEL = "gpt-4.1-mini"