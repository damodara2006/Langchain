from google.genai import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Create client with API key
client = Client(api_key=os.getenv("GEMINI_API"))

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)   