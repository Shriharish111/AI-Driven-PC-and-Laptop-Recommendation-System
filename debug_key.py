from dotenv import load_dotenv
import os

load_dotenv()
from app import app
from services.gemini_service import client

with app.app_context():
    app_key = os.getenv("GEMINI_API_KEY")
    client_key = client.api_key
    
    print(f"App OS Env Key:  '{app_key}'")
    print(f"Gemini Client Key: '{client_key}'")
    
    if app_key == client_key:
        print("MATCH: The Gemini client is using the .env key.")
    else:
        print("MISMATCH: The Gemini client is NOT using the .env key!")
