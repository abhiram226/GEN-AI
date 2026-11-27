from dotenv import load_dotenv
from google import genai
from google.genai import errors
import time
import os

#Loading api key
load_dotenv()

#Reading api key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found")

#initializing gemini client
client = genai.Client(api_key = api_key)

#Making first LLM call
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

#Displaying response
print("\nLLM Response: ")
print(response.text)