import os
from dotenv import load_dotenv
from google import genai
import google.genai.errors

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"Testing API Key starting with: {api_key[:10]}...")

try:
    # Initialize the client
    client = genai.Client(api_key=api_key)

    # Make a simple request
    print("Sending request to gemini-2.5-flash-lite...")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Say hello in exactly one word."
    )
    
    print("\nSUCCESS! API is working.")
    print(f"Response: {response.text}")

except google.genai.errors.ClientError as e:
    print(f"\nCLIENT ERROR OCCURRED:\n{e}")
except Exception as e:
    print(f"\nUNEXPECTED ERROR OCCURRED:\n{e}")
