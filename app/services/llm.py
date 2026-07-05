from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.config import Config


class LLMService:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=Config.GROQ_API_KEY,
            model="llama-3.3-70b-versatile",
            temperature=0.2
        )

    def generate_json(self, prompt: str, schema):

        parser = JsonOutputParser(pydantic_object=schema)

        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an AI assistant that ALWAYS returns valid JSON.",
                ),
                ("human", "{input}"),
            ]
        )

        chain = prompt_template | self.llm | parser

        return chain.invoke(
            {
                "input": prompt
            }
        )

    def generate_text(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content


llm = LLMService()