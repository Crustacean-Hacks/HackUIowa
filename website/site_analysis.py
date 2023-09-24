import openai, os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

openai.api_key = os.environ.get("OPENAI_API_KEY")

def categorize_website(site: str) -> str:
    chat = openai.Completion.create(
        model = "text-ada-001",
        messages = [
            {"text": """Categorize this website into Ecommerce, personal, entertainment, social, productivity, finance, education, health, 
             news and information, or MISC: """ + site, "user": "human",},
        ]
    )
    return chat["choices"][0]["text"]
