from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def query(user_input: list[dict[str, str]]) -> str:

    response = client.chat.completions.create(model="gpt-4o-mini", messages=user_input)

    reply = response.choices[0].message.content

    return reply
