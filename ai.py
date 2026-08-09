from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel


class AICard(BaseModel):
    front: str
    back: str


class AIDeck(BaseModel):
    name: str
    cards: list[AICard]


load_dotenv()

client = OpenAI()


def generate_deck(topic: str) -> AIDeck:
    response = client.responses.parse(
        model="gpt-5-mini",

        input=[
            {
                "role": "developer",
                "content": """
                You are Cardlet's flashcard generation AI.

                Create accurate educational flashcards.

                Rules:
                - Each card should test one concept.
                - Avoid duplicate cards.
                - Questions should be clear and concise.
                - Answers should be accurate but easy to understand
                - Only include information relevant to the requested topic.
                
                Input formats:
                - There are two types of expected inputs
                    1) A general theme, generate flashcards relating to the theme
                    2) A source (e.g. a paragraph of text), generate flashcards based on the source
                - The input will be provided in the "content" field of the user message.
                """
            },
            {
                "role": "user",
                "content": f"""Create a flashcard deck about: {topic}"""
            }
        ],

        text_format=AIDeck
    )

    return response.output_parsed
