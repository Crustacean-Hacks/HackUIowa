import openai, os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

openai.api_key = os.environ.get("OPENAI_API_KEY")


def categorize_website(site: str) -> str:
    chat = openai.Completion.create(
        model="text-curie-001",
        prompt="Categorize this website into ONE of the following: Ecommerce, personal, entertainment, social, productivity, finance, education, health, news and information, or misc:"
        "" + site + "   ... Just give me the top category. If you cannot categorize something, just give it misc, such as example.com should be misc.",
    )
    return chat.choices[0].text.strip()
