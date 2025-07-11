from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api = os.getenv("OPEN_ROUTER_KEY")

client = AsyncOpenAI(
    api_key=gemini_api,
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    model="google/gemini-2.0-flash-exp:free",
    openai_client=client
)

