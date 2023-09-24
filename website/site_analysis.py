import openai, os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

openai.api_key = os.environ.get("OPENAI_API_KEY")


def categorize_website(site: str) -> str:
    chat = openai.Completion.create(
        model="babbage-002",
        prompt="Categorize this website into exactly ONE of the following categories: [Ecommerce, Personal, Entertainment, Social, Productivity, Finance, Education, Health, News, Information, Miscellaneous]:"
        "" + site + "   ... You MUST choose exactly one category from above.",
    )
    return chat.choices[0].text.strip()
