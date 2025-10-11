import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("INFOMANIAK_API_TOKEN")
PRODUCT_ID = os.getenv("INFOMANIAK_PRODUCT_ID")

if not OPENAI_API_KEY or not PRODUCT_ID:
    raise EnvironmentError("Missing environment variables for API setup.")

INFOMANIAK_BASE_URL = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai"
client = OpenAI(api_key=OPENAI_API_KEY, base_url=INFOMANIAK_BASE_URL)

VALID_MODELS = [
    'mixtral', 'mixtral8x22b', 'llama3', 'granite', 'reasoning',
    'mistral24b', 'mistral3', 'qwen3', 'gemma3n', 'Qwen/Qwen3-Coder-480B-A35B-Instruct'
]
DEFAULT_MODEL = VALID_MODELS[0]
