import openai, os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

openai.api_key = os.environ.get("OPENAI_API_KEY")


def categorize_website(site: str) -> str:
    chat = openai.Completion.create(
        model="text-curie-001",
        prompt="Categorize this website into ONE of the following: Ecommerce, personal, entertainment, social, productivity, finance, education, health, news and information, or MISCsite:"
        "" + site + "   ... Just give me the top category.",
    )
    return chat.choices[0].text.strip()

